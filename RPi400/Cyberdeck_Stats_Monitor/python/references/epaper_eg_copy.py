#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
# picdir is /home/kfctr400/omgitskuei/RPiDev/RPi400/Cyberdeck_Stats_Monitor/pic
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
# libdir is /home/kfctr400/e-Paper/RaspberryPi_JetsonNano/python/lib
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V3
import time
from PIL import Image, ImageDraw, ImageFont
# import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V3 Demo")
    
    epd = epd2in13_V3.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    # For debugging purposes, draw two lines splitting the display into quads
        # draw.line([(0, (displayHeight/2)), (displayWidth, (displayHeight/2))], fill = 0,width = 1) # draw horizontal line spliting screen halfway down
        # draw.line([((displayWidth/2), 0),((displayWidth/2),122)], fill = 0,width = 1) # draw vertical line spliting screen down middle
    
#     draw.rectangle([(0,0),(50,50)],outline = 0)
    # Draw a black rectangle along the bottom half of the screen
    draw.rectangle([(0,61),(250,122)],fill = 0)
#     draw.line([(0,61),(250,61)], fill = 0,width = 1)
#     draw.line([(0,50),(50,0)], fill = 0,width = 1)
#     draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
#     draw.ellipse((55, 60, 95, 100), outline = 0)
#     draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
#     draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
#     draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
#     draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
#     draw.text((60, 15), 'e-Paper demo', font = font15, fill = 0)
    draw.text((110, 90), u'OmgItsKuei', font = font24, fill = 1)
    # image = image.rotate(180) # rotate
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    
    # read bmp file 
#     logging.info("2.read bmp file...")
#     image = Image.open(os.path.join(picdir + '/bmps', 'cpu_bmp.bmp'))
#     epd.display(epd.getbuffer(image))
#     time.sleep(2)
    
    # read bmp file on window
#     logging.info("3.read bmp file on window...")
    # epd.Clear(0xFF)
#     image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
#     bmp = Image.open(os.path.join(picdir + '/bmps', 'temp_bmp.bmp'))
#     image1.paste(bmp, (2,2))    
#     epd.display(epd.getbuffer(image1))
#     time.sleep(2)
    
    # # partial update
#     logging.info("4.show time...")
#     time_image = Image.new('1', (epd.height, epd.width), 255)
#     time_draw = ImageDraw.Draw(time_image)
#     
#     epd.displayPartBaseImage(epd.getbuffer(time_image))
#     num = 0
#     while (True):
#         time_draw.rectangle((120, 80, 220, 105), fill = 255)
#         time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
#         epd.displayPartial(epd.getbuffer(time_image))
#         num = num + 1
#         if(num == 5):
#             break
    
#     logging.info("Clear...")
#     epd.init()
#     epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.error(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V3.epdconfig.module_exit()
    exit()
