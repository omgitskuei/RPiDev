# Cyberdeck Stats Monitor for the Raspberry Pi 400
---
This Raspberry Pi 400 project displays CPU usage %, RAM usage %, Disk space used %, and CPU temperature on a Waveshare ePaper (250 x 122 pixels, 2.13 inch EPD HAT for Raspberry Pi, Black/White, RPI SPI interface) connected to a Adafruit Cyberdeck Bonnett (which then connects to the Raspberry Pi 400's GPIO).
The scripts clear.py (clears the display) and cyberdeck_stats_monitor.py (gets and writes data onto the display) are written in python.

### Limitations
---
This project has not been tested on other Raspberry Pi models besides Raspberry Pi 400, but if the OS is Raspberry Pi OS (Bullseye) then it should work.
The cyberdeck_stats_monitor.py python script relies on os.popen() which *might* make it compatible with Linux systems only.  

### Tutorial
---
##### _Components_
| Component name | Description | Link |
| ------ | ------ | ------ |
| Raspberry Pi 400 | A Raspberry Pi computer with a quad-core 64-bit processor, 4GB of RAM, wireless networking, dual-display output, and 4K video playback, as well as a 40-pin GPIO header. | [Raspberry Pi 400][rp400link] |
| Waveshare ePaper 2.13 inch Black/White display | Note there's multiple two-colored 2.13" ePaper displays from Waveshare - the component used here does not have the "(B)", "(C)", or "(D)" in its name. | [Waveshare ePaper 2.13" display][WaveshareEPDlink] |
| Adafruit Cyberdeck Bonnett | It's a plug-and-play HAT attached to the GPIO pins. For the Raspberry Pi 400, it attaches at a slant with the HAT's pins facing the user. It's called a 'bonnett' because it's about half the size of a regular HAT. | [Adafruit Cyberdeck Bonnett][Bonnettlink] |

### License
---
omgitskuei/RPiDev is licensed under the GNU General Public License v3.0.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 

Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

   [rp400link]: <https://www.raspberrypi.com/products/raspberry-pi-400-unit/>
   [WaveshareEPDlink]: <https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT>
   [Bonnettlink]: <https://www.adafruit.com/product/4862>
   
