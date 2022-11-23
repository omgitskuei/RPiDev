#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import configparser


# init logger
logging.basicConfig(level=logging.DEBUG)


# import necessary waveshare_epd library
logging.info("Retrieving python library for driving Waveshare 2.13in ePaper HAT...")
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'library')
if os.path.exists(libdir):
    sys.path.append(libdir)
    logging.info("Done.")
from waveshare_epd import epd2in13_V3


# read/create ini
config = configparser.ConfigParser()
ini_path = '../cyberdeck_stats_monitor_config.ini'
try:
    with open(ini_path) as ini:
        logging.info("Successfully opened ini file")
        config.read_file(ini)
except IOError:
    # ini file doesn't exist, so create ini file.
    logging.info("Failed to open ini file, Creating ini file")
    config['DEFAULT'] = {'version': '5',
                         'tempunit': 'c',
                         'enable': 'true'}
    config['Waveshare,ePaper,2.13in'] = {'displaywidth': '250',
                                         'displayheight': '122',
                                         'minimumrefresh': '3_mins'}
    with open(ini_path, 'w') as ini:
        config.write(ini)
    config.read(ini_path)

if config['DEFAULT']['enable'] == 'false':
    exit()


# main...
def main():
    try:
        logging.info("Clearing ePaper...")
        epd = epd2in13_V3.EPD()
        epd.init()
        # clear ePaper HAT display
        epd.Clear(0xFF)
        epd.sleep()
        
        logging.info("Done.")
        exit()
        
    except IOError as e:
        logging.error(e)
        
    except KeyboardInterrupt:    
        logging.info("User Pressed [Ctrl] + [c] - KeyboardInterrupt ending script...")
        epd2in13_V3.epdconfig.module_exit()
        
        logging.info("Done.")
        exit()

if __name__ == '__main__':
    main()
    