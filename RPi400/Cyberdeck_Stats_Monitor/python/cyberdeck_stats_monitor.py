#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import psutil
import gpiozero
import decimal
from PIL import Image, ImageDraw, ImageFont
import time

# init logger
logging.basicConfig(level=logging.DEBUG)

# import necessary waveshare_epd library
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
logging.info("Retrieving python library for driving Waveshare 2.13in ePaper HAT...")
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V3
logging.info("Done.")

# save path to .../RPiDev/RPi400/Cyberdeck_Stats_Monitor/pic
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

# init global vars
cpuTemp = 0.0
cpuUsage = 0.0
ramTot = ""
ramUsed = ""
ramFree = ""
diskUsage = 0
epd = None
# ePaper display dimension is 250x122
displayWidth = 250
displayHeight = 122

# Note: Returns str
def getCPUTemp_os():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Note: Returns float
def get_CPUUsage():
    return psutil.cpu_percent()

# Note: Returns RAM info (units in KB) as a list of str (Index 0: total RAM, Index 1: used RAM,  Index 2: free RAM)
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Note: Returns disk usage as a float
def get_diskUsage():
    return gpiozero.DiskUsage().usage

# Note: Takes a float and truncates it to one decimal places, returns the number as a decimal
def roundDownToOneDecimal(aFloat):
    return decimal.Decimal(aFloat).quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_DOWN)




# main...
def main():
    try:
        # get data
        logging.info("Getting CPU temperature...")
        # print(getCPUTemp_gpio())
        cpuTemp = getCPUTemp_os()
        print(cpuTemp  + "°C")
        logging.info("Done.")
        
        logging.info("Getting CPU usage...")
        cpuUsage = get_CPUUsage()
        print('{}%'.format(cpuUsage))
        logging.info("Done.")
        
        logging.info("Getting RAM usage...")
        ramInfo = getRAMinfo()
        ramTot = int(ramInfo[0])/1000
        ramUsed = int(ramInfo[1])/1000
        print('{}%'.format(roundDownToOneDecimal(ramUsed/ramTot*100)))
        logging.info("Done.")
        
        logging.info("Getting disk usage...")
        diskUsage = roundDownToOneDecimal(get_diskUsage())
        print('{}%'.format(diskUsage))
        logging.info("Done.")
        
        logging.info("Getting fonts...")
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        logging.info("Done.")
        
        logging.info("Clearing ePaper display...")
        epd = epd2in13_V3.EPD()
        epd.init()
        epd.Clear(0xFF)
        logging.info("Done.")
        
        logging.info("Writing bmp image into buffer...")
        # image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame 
        image = Image.open(os.path.join(picdir + '/bmps', 'combined.bmp'))
        draw = ImageDraw.Draw(image)
        logging.info("Done.")
        
        # For debugging purposes, draw two lines splitting the display into quads
        # draw.line([(0, (displayHeight/2)), (displayWidth, (displayHeight/2))], fill = 0,width = 1) # draw horizontal line spliting screen halfway down
        # draw.line([((displayWidth/2), 0),((displayWidth/2),122)], fill = 0,width = 1) # draw vertical line spliting screen down middle
        
        logging.info("Writing data into buffer...")
        topPadding = 15
        leftPadding = 50
        draw.text((leftPadding,                                0 + topPadding), cpuTemp  + "°C", font = font24, fill = 0)
        draw.text(((displayWidth/2) + leftPadding, 0 + topPadding), '{}%'.format(cpuUsage), font = font24, fill = 0)
        draw.text((leftPadding,                                (displayHeight/2) + topPadding), '{}%'.format(roundDownToOneDecimal(ramUsed/ramTot*100)), font = font24, fill = 0)
        draw.text(((displayWidth/2) + leftPadding, (displayHeight/2) + topPadding), '{}%'.format(diskUsage), font = font24, fill = 0)
        logging.info("Done.")
        
        logging.info("Displaying the buffer onto the ePaper")
        epd.display(epd.getbuffer(image))
        logging.info("Done.")
        
        time.sleep(3)
        
        logging.info("Putting ePaper display to sleep...")
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
    