#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging

# init logger
logging.basicConfig(level=logging.DEBUG)

# import necessary waveshare_epd library
logging.info("Retrieving python library for driving Waveshare 2.13in ePaper HAT...")
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
# libdir is "[...]/RPiDev/RPi400/Cyberdeck_Stats_Monitor/lib"
if os.path.exists(libdir):
    sys.path.append(libdir)
    logging.info("Done.")
        
from waveshare_epd import epd2in13_V3

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
    