
import os
import logging
import ConfigParser
from optparse import OptionParser

version = "0.0.1"

def run():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage, version=version)

    parser.add_option("-f", "--file", dest="configfile",
    		help="read configuration from CONFIGFILE."
    		"defaults to /etc/dreidel.conf",
    		default="/etc/dreidel.conf")

    parser.add_option("-s", "--statusfile", dest="statusfile",
    		help="write status to file 0=exit ok, 1=running, 2=exit error",
    		default=None)

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

    ## TODO: STATUSFILE

    #read configfile
    config = ConfigParser.SafeConfigParser()
    config.read(options.configfile)

    if len(config.sections()) == 0:
    	msg = "no configuration found at location "+options.configfile
    	logging.error(msg)
    	logging.info("dreidel stopped")
    	logging.shutdown()
    	parser.error(msg)

    for s in config.sections():

        (p,f) = os.path.split(s)

        destination_path = p
        if config.has_option(s, "olddir"):
            destination_path = config.get(s, "olddir")
        print p
        print f
        print "############"
        print destination_path



    # echo 0 to statusfile TODO!
    logging.info("dreidel stopped")
    logging.shutdown()