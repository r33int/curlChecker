from configparser import ConfigParser
from argparse import ArgumentParser
import os.path
import pycurl
import linecache

## Parse arguments
parser = ArgumentParser()
parser.add_argument("-i", "--in", dest="input", help="Open specified file")
parser.add_argument("-o", "--out", dest="output", help="Write to specified file")
args = parser.parse_args()
input = args.input
output = args.output

## Parse and set config
cfg = ConfigParser()
cfg.read('config.ini')
VERBOSE = cfg.getboolean('curl', 'verbose')
TIMEOUT = cfg.get('curl', 'timeout_delay')
USERNAME = cfg.get('credentials', 'username')
PASSWORD = cfg.get('credentials', 'password')

## Check number of lines
num_lines = sum(1 for line in open(input))
progress = (1)

# The actual process
for i in range(num_lines):
    line = linecache.getline(input, progress).rstrip('\n')
    try:
        c = pycurl.Curl()
        c.setopt(c.URL, line)
        c.setopt(c.VERBOSE, bool(VERBOSE))
        c.setopt(c.TIMEOUT, int(TIMEOUT))
        c.setopt(c.USERPWD, USERNAME + ':' + PASSWORD)
        c.perform()
        c.close()
    # When curl fails
    except pycurl.error:
        print(line, "has failed connecting!")
        continue
    # When curl succeeds
    else:
        print(line, "has successfully connected, writing to successful URLs log!")
        fp = open(output, 'a')  
        fp.write(line + '\n')
    # Increment line progress and start the process over
    progress += (1)