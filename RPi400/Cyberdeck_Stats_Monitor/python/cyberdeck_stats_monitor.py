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

logging.basicConfig(level=logging.DEBUG)

logging.info("Retrieving python library for driving Waveshare 2.13in ePaper HAT...")
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                      'library')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V3

logging.info("Done.")

logging.info("Get path for /pic...")
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                      'pic')
logging.info("Done.")


# Note: Returns str, add "°C" to the result
def get_gpu_temp_via_os():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


# Note: Returns float, add "%" to the result
def get_cpu_usage():
    return str(psutil.cpu_percent())


# Note: Returns RAM info (units in bytes) as a dict
def get_ram_info():
    ram_info_raw = psutil.virtual_memory()
    return {"percent": ram_info_raw[2]}


# Note: Returns disk usage as a float
def get_disk_usage():
    return str(round_down_to_one_decimal(gpiozero.DiskUsage().usage))


# Note: Takes a float and truncates it to one decimal places, returns the number
# as a decimal
def round_down_to_one_decimal(a_float):
    return decimal.Decimal(a_float).quantize(decimal.Decimal('.1'),
                                             rounding=decimal.ROUND_DOWN)


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
        cpu_temp = '{}°C'.format(get_gpu_temp_via_os())
        logging.info(cpu_temp)
        logging.info("Done.")

        logging.info("Getting CPU usage...")
        cpu_usage = '{}%'.format(get_cpu_usage())
        logging.info(cpu_usage)
        logging.info("Done.")

        logging.info("Getting RAM usage...")
        ram_info = '{}%'.format(get_ram_info()['percent'])
        logging.info(ram_info)
        logging.info("Done.")

        logging.info("Getting disk usage...")
        disk_usage = '{}%'.format(get_disk_usage())
        logging.info(disk_usage)
        logging.info("Done.")

        logging.info("Getting timestamp...")
        time = str(datetime.now())[0:str(datetime.now()).index('.')]
        logging.info(time)
        logging.info("Done.")

        logging.info("Getting IP address...")
        # NOTE: ends with a SPACE and an ENTER, need to remove last 2 chars
        ip = os.popen('hostname -I').readline()[0:-2]
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
        top_padding = 15
        left_padding = 50
        # top row - CPU usage %, CPU temperature
        draw.text((left_padding, 0 + top_padding),
                  cpu_usage,
                  font=font24,
                  fill=0)
        draw.text((120 + left_padding, 0 + top_padding),
                  cpu_temp,
                  font=font24,
                  fill=0)
        # middle row - RAM usage %, Disk used %
        draw.text((left_padding, 45 + top_padding),
                  ram_info,
                  font=font24,
                  fill=0)
        draw.text((120 + left_padding, 45 + top_padding),
                  disk_usage,
                  font=font24,
                  fill=0)
        # bottom row - Timestamp, IP address
        draw.text((5, 85 + top_padding),
                  time[0:-3] + ((" | " + ip) if (ip is None or len(ip) > 0) else ""),
                  font=font13,
                  fill=0)  # remove seconds, if no ip then ""
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
        logging.info("User Pressed [Ctrl] + [c]. KeyboardInterrupt ending script...")
        epd2in13_V3.epdconfig.module_exit()
        logging.info("Done.")
        exit()


if __name__ == '__main__':
    main()
