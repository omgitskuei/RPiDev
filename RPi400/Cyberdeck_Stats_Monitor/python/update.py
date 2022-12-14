#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import psutil
import gpiozero
import decimal
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import configparser
import traceback
import RPi.GPIO as GPIO

logging.basicConfig(level=logging.DEBUG)

# get /library directories
logging.info('Getting path for /library containing ePaper HAT display module...')
lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                      'library')
if os.path.exists(lib_dir):
    sys.path.append(lib_dir)
    logging.info('lib_dir={}'.format(lib_dir))
else:
    logging.info('ePaper HAT display module not found at {}. Exiting program.'.format(lib_dir))
    exit()
from waveshare_epd import epd2in13_V3
logging.info('Done.')


# get /pic directories
logging.info('Getting path for /pic containing bmp files, fonts, photos...')
pic_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                      'pic')
logging.info('pic_dir={}'.format(pic_dir))
logging.info('Done.')


# read/create config ini file
logging.info('Reading .ini file with configparser...')
config = configparser.ConfigParser()
ini_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/cyberdeck_stats_monitor_config.ini'
logging.info('ini_path={}'.format(ini_path))
try:
    with open(ini_path) as ini:
        config.read_file(ini)
        logging.info('Successfully opened ini file')
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
            logging.info('Display not plugged in')
        else:
            logging.info('Display is plugged in')
            pluggedIn = True
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt thrown when evaluating if display is plugged in. Returning False to exit program.')
        pluggedIn = False
    finally:
        logging.info('Done')
        GPIO.cleanup()
        return pluggedIn
    
   

        
# Note: Takes a float and truncates it to one decimal places, returns the number
# as a decimal
def round_down_to_one_decimal(a_float):
    return decimal.Decimal(a_float).quantize(decimal.Decimal('.1'),
                                             rounding=decimal.ROUND_DOWN)


# Returns raw data values
def retrieve_raw_data():
    logging.info('Getting raw data...')
    raw = {
        'cpu_temp' : round_down_to_one_decimal(gpiozero.CPUTemperature().temperature),
        'cpu_usage' : psutil.cpu_percent(),
        'ram_used' : psutil.virtual_memory()[2],
        'disk_used' : round_down_to_one_decimal(gpiozero.DiskUsage().usage),
        'timestamp' : datetime.now(),
        'ip' : os.popen('hostname -I').readline()
    }
    logging.info('Done.')
    return raw


def get_cpu_temp(raw_data_map):
    logging.info('Getting CPU temperature...')
    try:
        unit = config['DEFAULT']['tempunit']
        logging.info('Temperature unit set by ini file to {}'.format(unit))
        switch={
          'c': str(raw_data_map['cpu_temp']) + '??C',
          'f': str(round_down_to_one_decimal(float(raw_data_map['cpu_temp']) * 1.8) + 32) + '??F'
        }
        cpu_temp = switch.get(unit,'Invalid')
    except NameError:
        traceback.print_exc(limit=None, file=None, chain=False)
        logging.error('NameError thrown getting CPU temp, defaulting to Celsius')
        cpu_temp = str(raw_data_map['cpu_temp']) + '??C'
    logging.info(cpu_temp)
    logging.info('Done.')
    return cpu_temp


def get_cpu_usage(raw_data_map):
    logging.info('Getting CPU usage...')
    cpu_usage = '{}%'.format(raw_data_map['cpu_usage'])
    logging.info(cpu_usage)
    logging.info('Done.')
    return cpu_usage


def get_ram_used(raw_data_map):
    logging.info('Getting RAM usage...')
    ram_info = '{}%'.format(raw_data_map['ram_used'])
    logging.info(ram_info)
    logging.info('Done.')
    return ram_info


def get_disk_used(raw_data_map):
    logging.info('Getting disk usage...')
    disk_used = '{}%'.format(raw_data_map['disk_used'])
    logging.info(disk_used)
    logging.info('Done.')
    return disk_used


def get_time(raw_data_map):
    logging.info('Getting timestamp...')
    time = str(raw_data_map['timestamp'])[0:str(raw_data_map['timestamp']).index('.')][0:-3]
    logging.info(time)
    logging.info('Done.')
    return time


def get_ip(raw_data_map):
    logging.info('Getting IP address...')
    # NOTE: ends with a SPACE and an ENTER, need to remove last 2 chars
    ip = raw_data_map['ip'][0:-2]
    try:
        ip = ip[0:ip.index(' ')]
    except ValueError as ve:
        pass
    logging.info(ip)
    logging.info('Done.')
    return ip

# main...
def main():
    if isDisplayPluggedIn():
        pass
    else:
        logging.info('Exiting Program.')
        exit()
    
    try:
        # init display
        logging.info('Initializing ePaper display...')
        epd = epd2in13_V3.EPD()
        epd.init()
        logging.info('Done.')

        # get data
        raw_data_map = retrieve_raw_data()
        
        # init fonts
        logging.info('Getting fonts...')
        font24 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 24)
        font13 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 14)
        logging.info('Done.')

        # draw display
        logging.info('Writing bmp image into buffer...')
        image = Image.open(os.path.join(pic_dir + '/bmps', 'combined.bmp'))
        draw = ImageDraw.Draw(image)
        logging.info('Done.')

        logging.info('Writing stats data into buffer...')
        top_padding = 15
        left_padding = 50
        # top row - CPU usage %, CPU temperature
        draw.text((left_padding, 0 + top_padding),
                  get_cpu_usage(raw_data_map),
                  font=font24,
                  fill=0)
        draw.text((120 + left_padding, 0 + top_padding),
                  get_cpu_temp(raw_data_map),
                  font=font24,
                  fill=0)
        # middle row - RAM usage %, Disk used %
        draw.text((left_padding, 43 + top_padding),
                  get_ram_used(raw_data_map),
                  font=font24,
                  fill=0)
        draw.text((120 + left_padding, 43 + top_padding),
                  get_disk_used(raw_data_map),
                  font=font24,
                  fill=0)
        # bottom row - Timestamp, IP address
        ip = get_ip(raw_data_map)
        draw.text((5, 85 + top_padding),
                  get_time(raw_data_map) + ((' | ' + ip) if (ip is None or len(ip) > 0) else ''),
                  font=font13,
                  fill=0)  # remove seconds, if no ip then ''
        logging.info('Done.')

        logging.info('Displaying the buffer onto the ePaper')
        epd.display(epd.getbuffer(image))
        logging.info('Done.')

        # sleep
        logging.info('Putting ePaper display to sleep...')
        epd.sleep()
        logging.info('Done. Exiting program.')
        exit()

    except IOError as e:
        logging.error(e)
        logging.info('Exiting program.')
        exit()

    except KeyboardInterrupt:
        logging.info('User Pressed [Ctrl] + [c]. KeyboardInterrupt ending script...')
        logging.info('Exiting program.')
        exit()


if __name__ == '__main__':
    main()
