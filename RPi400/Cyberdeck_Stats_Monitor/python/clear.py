#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import configparser
import RPi.GPIO as GPIO

# init logger
logging.basicConfig(level=logging.DEBUG)


# import necessary waveshare_epd library
logging.info('Getting path for ../library containing ePaper HAT display module...')
lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'library')
if os.path.exists(lib_dir):
    sys.path.append(lib_dir)
    logging.info('lib_dir={}'.format(lib_dir))
else:
    logging.info('ePaper HAT display module not found at {}. Exiting program.'.format(lib_dir))
    exit()
from waveshare_epd import epd2in13_V3
logging.info('Done.')

# read/create ini
logging.info('Reading .ini file with configparser...')
config = configparser.ConfigParser()
ini_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/cyberdeck_stats_monitor_config.ini'
logging.info('ini_path={}'.format(ini_path))
try:
    with open(ini_path) as ini:
        logging.info('Successfully opened ini file')
        config.read_file(ini)
except IOError:
    # ini file doesn't exist, so create ini file.
    logging.info('Failed to open ini file, Creating ini file')
    config['DEFAULT'] = {'version': '5',
                         'tempunit': 'c',
                         'enable': 'true'}
    config['Waveshare,ePaper,2.13in'] = {'displaywidth': '250',
                                         'displayheight': '122',
                                         'minimumrefresh': '3_mins'}
    with open(ini_path, 'w') as ini:
        config.write(ini)
    config.read(ini_path)
# check if disabled by ini file
if config['DEFAULT']['enable'] == 'false':
    logging.info('Ini file.enable currently set to false. Exiting program.')
    exit()
logging.info('Done.')

# check if display is plugged into GPIO
def isDisplayPluggedIn():
    logging.info('Checking if display is plugged in...')
    pluggedIn = False
    try:
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if GPIO.input(17) == GPIO.HIGH:
            logging.info("Display not plugged in")
        else:
            logging.info("Display is plugged in")
            pluggedIn = True
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt thrown when evaluating if display is plugged in. Returning False to exit program.')
        return False
    finally:
        GPIO.cleanup()
    logging.info('Done.')
    return pluggedIn


# main...
def main():
    if isDisplayPluggedIn():
        pass
    else:
        logging.info('Exiting Program.')
        exit()
        
    try:
        logging.info('Clearing ePaper...')
        epd = epd2in13_V3.EPD()
        epd.init()
        # clear ePaper HAT display
        epd.Clear(0xFF)
        epd.sleep()
        
        logging.info('Done. Exiting program.')
        exit()
        
    except IOError as e:
        logging.error(e)
        epd2in13_V3.epdconfig.module_exit()
        logging.info('Exiting program.')
        exit()
        
    except KeyboardInterrupt:    
        logging.info('User Pressed [Ctrl] + [c] - KeyboardInterrupt ending script...')
        epd2in13_V3.epdconfig.module_exit()
        logging.info('Exiting program.')
        exit()

if __name__ == '__main__':
    main()
    