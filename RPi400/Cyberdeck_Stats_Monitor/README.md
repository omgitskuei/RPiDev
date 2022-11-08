# Cyberdeck Stats Monitor for the Raspberry Pi 400
---

![titlepic](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v4.JPG?raw=false "Title image")

This Raspberry Pi 400 project displays ...
- CPU usage %, 
- RAM usage %, 
- Disk space used %, 
- CPU temperature, 
- machine ip address, 
- and timestamp 
... on a Waveshare ePaper (250 x 122 pixels, 2.13 inch EPD HAT for Raspberry Pi, Black/White, RPI SPI interface) connected to a Adafruit Cyberdeck Bonnett (which then connects to the Raspberry Pi 400's GPIO).
The scripts clear.py (clears the display) and cyberdeck_stats_monitor.py (gets and writes data onto the display) are written in python.

## Limitations
---
This project has not been tested on other Raspberry Pi models besides Raspberry Pi 400, but if the OS is Raspberry Pi OS (Bullseye) then it should work.
The cyberdeck_stats_monitor.py python script relies on os.popen() which **might** make it compatible with Linux systems only.  

## Tutorial
---
### _Components_
| Component name | Description | Link | Importance |
| ------ | ------ | ------ | ------ |
| Raspberry Pi 400 | A Raspberry Pi computer with a quad-core 64-bit processor, 4GB of RAM, wireless networking, dual-display output, and 4K video playback, as well as a 40-pin GPIO header. | [Raspberry Pi 400][rp400link] | Necessary |
| Waveshare ePaper 2.13 inch Black/White display | Note there's multiple two-colored 2.13" ePaper displays from Waveshare - the component used here does not have the "(B)", "(C)", or "(D)" in its name. | [Waveshare ePaper 2.13" display][WaveshareEPDlink] | Necessary |
| Adafruit Cyberdeck Bonnett | It's a plug-and-play HAT attached to the GPIO pins. For the Raspberry Pi 400, it attaches at a slant with the HAT's pins facing the user. It's called a 'bonnett' because it's about half the size of a regular HAT. | [Adafruit Cyberdeck Bonnett][Bonnettlink] | Necessary |

### _Guide_
1. Get the necessary components ready.

![guidepic1](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic1.JPG?raw=false "Guide, Step 1")

2. Download some version of python 3.

![guidepic2](https:// "Guide, Step 2")

3. Download the folder `Cyberdeck_Stats_Monitor`. Some contents served as reference material or original assets used for the creation of this project - these can be deleted to save space without affecting the project. :heavy_exclamation_mark: See Appendix A for details.

![guidepic3](https:// "Guide, Step 3")

4. Add a crontab job to run the clear.py script on reboot (reboot startup as well as restart) - requires Linux system to use crontab. To get this step to work on Windows/Mac, an equivalent to crontab is needed.

![guidepic4](https:// "Guide, Step 4")

5. Add a crontab job to run the cyberdeck_stats_monitor.py script immediately on startup. This is because a repeating crontab job does not run until its interval has elapsed at least once. Without doing this step, the display would not start until 5 minutes after startup.

![guidepic5](https:// "Guide, Step 5")

6. Add a crontab job to run the cyberdeck_stats_monitor.py script every 5 minutes. This interval can be modified to the user's liking. That said, Waveshare recommends refresh intervals between 3 minutes and 24 hours. :heavy_exclamation_mark: See Appendix B for details and other precautions.

![guidepic6](https:// "Guide, Step 6")

7. Add a systemd unit file configured to run the clear.py script right before shutdown - requires Linux system to use systemd. For other OS, an equivalent to running the python script right before shutdown is needed. :heavy_exclamation_mark: See Appendix C for proper storage.

![guidepic7](https:// "Guide, Step 7")


#### _Appendix_
<details>
  <summary>Appendix A</summary>
  <p>The python scripts clear.py and cyberdeck_stats_monitor.py rely a specific file structure to import Waveshare ePaper display's library and to read essential bmp files.
  The /library folder, /python, and /pic folders need to remain in the same relative file system position to each other.
  
  ##### _Essentials files and folders_
  Files not listed in this tree can be deleted without consequence to the project.
  
    .
    ├── /library
        ├── /waveshare_epd
	        ├── epd2in13_V3.py
    ├── /pic
        ├── Font.ttc
        ├── /bmps
            ├── combined.bmp
    ├── /python
        ├── clear.py
        ├── cyberdeck_stats_monitor.py
  
  </p>
</details>

<details>
  <summary>Appendix B</summary>
  <p>Waveshare's manual cautions users of the ePaper display that keeping the display powered on for long durations will cause irreparable damage - after updating is complete, the display should be powered off or set to sleep mode. Running the cyberdeck_stats_monitor.py performs the update followed by immediately setting the screen to sleep.
  Waveshare recommends a refresh interval range between 3 mins minimum and 24 hours maximum and that the screen be cleared before storing.
  Note: this discussion of intervals is for Refreshes, not Partial Refreshes.
  Refresh uses `epd.display(epd.getbuffer(image))` while Partial Refresh uses `epd.displayPartBaseImage(epd.getbuffer(image))` to display static background, then `epd.displayPartial(epd.getbuffer(image))` to dynamically display the difference. |
  To demonstrate partial refresh, the demo python script provided by Waveshare iterated through a while-loop every 1 second to update a timestamp. Sleep `epd.sleep()` was not called before the next interval started - this means the display would be constantly powered on despite Waveshare's own warnings against constantly powering on the display. While the manual did not explicitly say that partial refreshing without sleep over a long time would (or would not) cause damage, it did say that partial refreshing should only be done "several" times before a full refresh. Exactly how many is several wasn't stated.
  From 10 repeated testings of the display with the demo, the demo provided's one-second interval partial refresh did not provide good consistent results. Sometimes the interval would be a second, other times slightly shorter or longer, depending on the execution speed of the software. Adding a 3 second delay between intervals also did not provide consistent results.
  For this project, considering the vague guidelines on partial refreshing and its mixed results from the demo, in order to preserve the service life of the ePaper display, it was decided that no partial refresh would be used.
  </p>
</details>

<details>
  <summary>Appendix C</summary>
  <p>Waveshare's manual points out that clearing the display before storage is important. 
  Under "Manual > Overview > Working Principle";
  > ... charged nanoparticles suspended in a liquid migrate under the action of an electric field
  Under "Manual > Resources > Datasheet > 2.13inch e-Paper Specification V3 (pdf) > 16. Precautions";
  > ... "If the Module is not refreshed every 24 hours, a phenomena known as "Ghosting" or "Image Sticking" may occur. It is recommeded that customers store ... with a completely white image to avoid this issue. 
  </p>

## License
---
omgitskuei/RPiDev is licensed under the GNU General Public License v3.0.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 

Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

   [rp400link]: <https://www.raspberrypi.com/products/raspberry-pi-400-unit/>
   [WaveshareEPDlink]: <https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT>
   [Bonnettlink]: <https://www.adafruit.com/product/4862>
   
