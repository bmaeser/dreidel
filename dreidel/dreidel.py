#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import gzip
import shutil
import subprocess
import logging
import ConfigParser
from optparse import OptionParser
from datetime import date, timedelta

version = "1.0.2"

def run():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage, version=version)

    parser.add_option("-f", "--file", dest="configfile",
    		help="read configuration from CONFIGFILE."
    		"defaults to /etc/dreidel/dreidel.conf",
    		default="/etc/dreidel/dreidel.conf")
    parser.add_option("-l", "--logfile", dest="logfile",
    		help="logfile location. defaults to /var/log/dreidel.log",
    		default="/var/log/dreidel.log")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
    		default=False, help="make a lot of noise at the logfile")
    
    
    (options, args) = parser.parse_args()

    if options.verbose:
 	   logging.basicConfig(
    		filename=options.logfile,
    		format= "%(asctime)s [%(levelname)-8s] %(message)s",
    		level=logging.INFO)
    else:
    	logging.basicConfig(
    		filename=options.logfile,
    		format= "%(asctime)s [%(levelname)-8s] %(message)s")

    logging.info("dreidel started")

    #read configfile
    config = ConfigParser.SafeConfigParser()
    config.read(options.configfile)

    # skip, if configfile is empty
    if len(config.sections()) == 0:
    	msg = "no configuration found at location "+options.configfile
    	logging.error(msg)
    	logging.info("dreidel stopped")
    	logging.shutdown()
    	parser.error(msg)

    # iterate over all sections
    for s in config.sections():

        (p,filename) = os.path.split(s)

        destination_path = p
        if config.has_option(s, "olddir"):
            destination_path = config.get(s, "olddir")

        target_date = date.today()

        #set target date to yesterday if so in config
        if config.has_option(s, "date"):
            if config.get(s, "date") == "yesterday":
                target_date = target_date - timedelta(1)

        target_filename = target_date.strftime('%Y-%m-%d') + '-' +filename

        target_file = os.path.join(destination_path, target_filename)

        #run prerotate-command
        if config.has_option(s, "prerotate"):
            cmd = config.get(s, "prerotate")
            logging.info("executing prerotate command "+ cmd)
            subprocess.call(cmd, shell=True)

        
        if os.path.exists(target_file):
            #don't rotate the file, if target exists
            logging.error(target_file+" already exists. stop rotating")
            continue
        else:
            try:
                shutil.move(s, target_file)
            except IOError:
                logging.error("No such file "+s+" or orlddir does not exist")
                continue
        
        if config.has_option(s, "postrotate"):
            cmd = config.get(s, "postrotate")
            logging.info("executing postrotate command "+ cmd)
            subprocess.call(cmd, shell=True)
        
        #delete-pattern if compress = false
        delete_file_pattern = filename

        #compress defaults to True
        comp = True
        if config.has_option(s, "compress"):
            comp = config.getboolean(s, "compress")
                
        if comp:
            logging.info("Compressing "+ target_file)
            subprocess.call("gzip "+target_file, shell=True)

            #delete-pattern if compress = true
            delete_file_pattern = filename+".gz"

        rotation = 0
        if config.has_option(s, "rotate"):
            rotation = config.getint(s, "rotate")

        if rotation > 0:
            logging.info("deleting old logfiles")
            filelist_all = os.listdir(destination_path)

            filelist_target = []

            # extract all files in dir that belong to this logfile
            pattern = re.compile('^\d{4}-\d{2}-\d{2}-%s$'%delete_file_pattern)
            for f in filelist_all:
                if pattern.match(f) is not None:
                    filelist_target.append(f)

            print filelist_target

            filelist_target.sort()
            filelist_target.reverse()

            #remove all files from deletion-list that should not be deleted
            del filelist_target[0:rotation]
            print filelist_target

            for delfile in filelist_target:
                os.remove(os.path.join(destination_path, delfile))

    logging.info("dreidel stopped")
    logging.shutdown()

if __name__ == '__main__':
    sys.exit(run())