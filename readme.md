# Dreidel
A python replacement for logrotate

## Installation
#### with pip
	pip install dreidel
#### or checkout the github-branch
	git clone git://github.com/bmaeser/dreidel.git
	cd dreidel
	python setup.py install

## Usage
By default dreidel expects a configfile at /etc/dreidel/dreidel.conf, but you can specify a custom location with the -f (--file) option.
#### Full list of command line-options:
	Usage: dreidel.py [options]

	Options:
	    --version             show program's version number and exit
		-h, --help            show this help message and exit
		-f CONFIGFILE, --file=CONFIGFILE
                        	  read configuration from CONFIGFILE.defaults to
                        /etc/dreidel.conf
 		-l LOGFILE, --logfile=LOGFILE
                        logfile location. defaults to /var/log/dreidel.log
 		-v, --verbose         make a lot of noise at the logfile


#### Configfile-format
A full example:

    [/path/to/file]
    compress=true #default to true
    olddir=/path/to/olddir #uncomment if you don't want to move files
    rotate=3 #nr of old versions to keep, 0=no rotation / nothing gets deleted
    date=yesterday #take the day before today # defaults to today
    prerotate=#command to be executed before the moment
    postrotate=#command to be executed after the moment


## Usage scenarios
Create 2 configfiles:
    touch /etc/dreidel/daily.conf
    touch /etc/dreidel/weekly.con
Let cron execute daily.conf every day at 00:00, and weekly.conf every sunday at 00:00.

### Scenario 1: nginx-logfile-rotation (daily)
todo
### Scenario 2: backup of /etc/ (weekly)
todo

## Contribute
pull request please :-)

## Licence
Copyright (c) 2012 Bernhard Mäser (bernhard.maeser@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.