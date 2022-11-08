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
cpuTemp = ""
cpuUsage = ""
ramTot = ""
ramUsed = ""
ramFree = ""
diskUsage = ""
time = ""
ip = ""
epd = None
# ePaper display dimension is 250x122
displayWidth = 250
displayHeight = 122

# Note: Returns str, add "°C" to the result
def getCPUTemp_os():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Note: Returns float, add "%" to the result
def get_CPUUsage():
    return str(psutil.cpu_percent())

# Note: Returns RAM info (units in bytes) as a dict
def getRAMinfo():
    ramInfo_raw = psutil.virtual_memory()
    return {
        # "total" : ramInfo_raw[0],
        # "available" : ramInfo_raw[1],
        "percent" : ramInfo_raw[2],
        # "used" : ramInfo_raw[3],
        # "free" : ramInfo_raw[4],
        # "active" : ramInfo_raw[5],
        # "inactive" : ramInfo_raw[6],
        # "buffers" : ramInfo_raw[7],
        # "cached" : ramInfo_raw[8],
        # "shared" : ramInfo_raw[9],
        # "slab" : ramInfo_raw[10],
        }

# Note: Returns disk usage as a float
def get_diskUsage():
    return str(roundDownToOneDecimal(gpiozero.DiskUsage().usage))

# Note: Takes a float and truncates it to one decimal places, returns the number as a decimal
def roundDownToOneDecimal(aFloat):
    return decimal.Decimal(aFloat).quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_DOWN)


# main...
def main():
    try:
        # init display
        logging.info("Initializing ePaper display...")
        epd = epd2in13_V3.EPD()
        epd.init()
        # epd.Clear(0xFF)
        logging.info("Done.")
        
        # get data
        logging.info("Getting CPU temperature...")
        cpuTemp = getCPUTemp_os()  + "°C"
        logging.info(cpuTemp)
        logging.info("Done.")
        
        logging.info("Getting CPU usage...")
        cpuUsage = '{}%'.format(get_CPUUsage()) 
        logging.info(cpuUsage)
        logging.info("Done.")
        
        logging.info("Getting RAM usage...")
        ramInfo = '{}%'.format(getRAMinfo()['percent'])
        logging.info(ramInfo)
        logging.info("Done.")
        
        logging.info("Getting disk usage...")
        diskUsage = '{}%'.format(get_diskUsage())
        logging.info(diskUsage)
        logging.info("Done.")
        
        logging.info("Getting timestamp...")
        time = str(datetime.now())[0:str(datetime.now()).index('.')]
        logging.info(time)
        logging.info("Done.")
        
        logging.info("Getting IP address...")
        ip = os.popen('hostname -I').readline()[0:-2] # NOTE: ends with a SPACE and an ENTER, need to remove last 2 chars
        logging.info(ip) 
        logging.info("Done.")
        
        # init fonts
        logging.info("Getting fonts...")
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font13 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
        logging.info("Done.")
        
        # draw display
        logging.info("Writing bmp image into buffer...")
        image = Image.open(os.path.join(picdir + '/bmps', 'combined.bmp'))
        draw = ImageDraw.Draw(image)
        logging.info("Done.")
        
        logging.info("Writing data into buffer...")
        topPadding = 15
        leftPadding = 50
        # top row - CPU usage %, CPU temperature
        draw.text((leftPadding,           0 + topPadding), cpuUsage, font = font24, fill = 0)
        draw.text((120 + leftPadding, 0 + topPadding), cpuTemp, font = font24, fill = 0)
        # middle row - RAM usage %, Disk used %
        draw.text((leftPadding,           45 + topPadding), ramInfo, font = font24, fill = 0)
        draw.text((120 + leftPadding, 45 + topPadding), diskUsage, font = font24, fill = 0)
        # bottom row - Timestamp, IP address
        draw.text((5,                             85 + topPadding), time[0:-3] + ((" | " + ip) if ((ip == None) or (len(ip) > 0)) else ""), font = font13, fill = 0) # remove seconds, if no ip then ""
        logging.info("Done.")
        
        logging.info("Displaying the buffer onto the ePaper")
        epd.display(epd.getbuffer(image))
        logging.info("Done.")
        
        # sleep
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
    