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
This project has not been tested with other Waveshare ePaper displays - though changing the library for the correct corresponding one should enable them to work.


## Tutorial
---
### _Components_
| Component name | Description | Link | Importance |
| ------ | ------ | ------ | ------ |
| Raspberry Pi 400 | A Raspberry Pi computer with a quad-core 64-bit processor, 4GB of RAM, wireless networking, dual-display output, and 4K video playback, as well as a 40-pin GPIO header. | [Raspberry Pi 400][rp400link] | Necessary |
| Waveshare ePaper 2.13 inch Black/White display | Note there's multiple two-colored 2.13" ePaper displays from Waveshare - the component used here does not have the "(B)", "(C)", or "(D)" in its name. | [Waveshare ePaper 2.13" display][WaveshareEPDlink] | Necessary |
| Adafruit Cyberdeck Bonnett | It's a plug-and-play HAT attached to the GPIO pins. For the Raspberry Pi 400, it attaches at a slant with the HAT's pins facing the user. It's called a 'bonnett' because it's about half the size of a regular HAT. | [Adafruit Cyberdeck Bonnett][Bonnettlink] | Necessary |

### _Guide_
1. Get the necessary components ready by plugging in the 3 components like shown in the photo - with the Bonnet connected to the Raspberry Pi 400's GPIO and the ePaper connected to the Bonnet with the ribbon on the Left of the display. The ePaper display should be a white blank - the photo is showing my Programmer handle OmgItsKuei by running a script that draws a black rectangle and writing in white over the rectangle. This script was used to practice using the Waveshare ePaper python library.

![guidepic1](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic1.JPG?raw=false "Guide, Step 1")


2. Download some version of python 3 and install it on your system. Raspberry Pi 400 with Raspberry Pi OS (Bullseye) can skip this step as Python 3 is already installed. Make sure to also download the python library for operating the ePaper. You can get this library from Waveshare's github repository at [Waveshare Epaper repo][ePaperRepo] or find it included in ```/RPiDev/RPi400/Cyberdeck_Stats_Monitor/library```.

![guidepic2](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic2.JPG?raw=false "Guide, Step 2")


3. Download the RPiDev repository to get the folder `Cyberdeck_Stats_Monitor`. The file structure of the folder `Cyberdeck_Stats_Monitor` must remain unchanged but some of it contents served as reference material or older versions of assets used for this project - these can be deleted to save space without affecting the project. :heavy_exclamation_mark: [See Appendix A for details][Apdx].

![guidepic3](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic3.JPG?raw=false "Guide, Step 3")


4. Start the Linux terminal emulator and input ```crontab -e``` to start up crontab and add/remove jobs. You'll see something like this picture. Add the missing white text.
- Add a crontab job to run the ```clear.py``` script on reboot (reboot startup as well as restart) - requires Linux system to use crontab. To get this step to work on Windows/Mac, an equivalent to the crontab program is needed. 
- Then, add a crontab job to run the ```cyberdeck_stats_monitor.py``` script immediately on startup. This is because a repeating crontab job does not run until its interval has elapsed at least once. Without doing this step, the display would not start until 5 minutes after startup.
- Lastly, add a crontab job to run the cyberdeck_stats_monitor.py script every 5 minutes. This interval can be modified to the user's liking. That said, Waveshare recommends refresh intervals between 3 minutes and 24 hours. :heavy_exclamation_mark: [See Appendix B for details and other precautions][Apdx]. If you want to execute the ```cyberdeck_stats_monitor.py``` script just once, the 'meat' of cyberdeck_stats_monitor.py needs to be wrapped in a loop so it stays running after executing it once - if you're doing this, pay attention to the Appendix B on how to implement ePaper. 


![guidepic4](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic4.png?raw=false "Guide, Step 4")


5. Add the systemd unit file ```cyberdeck_stats_monitor_systemd_unit.service``` configured to run the clear.py script right before shutdown - requires Linux system to use systemd. For other OS, an equivalent to running the pythothe script right before shutdown is needed. :heavy_exclamation_mark: [See Appendix C for proper storage][Apdx]. Start the Linux terminal emulator and input ```sudo cp [...]/Cyberdeck_Stats_Monitor/cyberdeck_stats_monitor_systemd_unit.service.
/etc/systemd/system```. Ignore the ```scrot``` commands - they're for taking this screenshot.
:heavy_exclamation_mark: The .service file shown in the screenshot is missing the [Install] config - see the file's contents [here][serviceFile] for the missing [Install] config.

![guidepic5](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic5_1.png?raw=false "Guide, Step 5")


6. Refresh the systemd configuration files with ```sudo systemctl daemon-reload```.


7. Enable the ```cyberdeck_stats_monitor_systemd_unit.service``` in ```/etc/systemd/system``` so that it runs at the next boot. 
Open the Linux terminal emulator and Input ```systemctl enable cyberdeck_stats_monitor_systemd_unit```.

![guidepic7](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic7_1.png?raw=false "Guide, Step 7")


8. Try running the ```cyberdeck_stats_monitor.py``` script. You should see something similar to the image below. At this point, the display should update itself with current stats every 5 minutes.

![guidepic6](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic8.JPG?raw=false "Guide, Step 8")







#### _Appendix_
<details>
  <summary>Appendix A</summary>
  <p>The python scripts clear.py and cyberdeck_stats_monitor.py rely a specific file structure to import Waveshare ePaper display's library and to read essential bmp files.
  The /library folder, /python, and /pic folders need to remain in the same relative file system position to each other.
  
  Files not listed in this tree *should* be fine to delete without consequence to the project to save space.
  
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
    ├── cyberdeck_stats_monitor_systemd_unit.service
  </p>
</details>

<details>
  <summary>Appendix B</summary>
  <p>Waveshare's manual cautions users of the ePaper display that keeping the display powered on for long durations will cause irreparable damage - after updating is complete, the display should be powered off or set to sleep mode. Running the cyberdeck_stats_monitor.py performs the update followed by immediately setting the screen to sleep. Waveshare recommends a refresh interval range between 3 mins minimum and 24 hours maximum and that the screen be cleared before storing.
  Note: this discussion of intervals is for Refreshes, not Partial Refreshes.

  Refresh uses `epd.display(epd.getbuffer(image))` while Partial Refresh uses `epd.displayPartBaseImage(epd.getbuffer(image))` to display static background, then `epd.displayPartial(epd.getbuffer(image))` to dynamically display the difference. To demonstrate partial refresh, the demo python script provided by Waveshare iterated through a while-loop every 1 second to update a timestamp. Sleep `epd.sleep()` was not called before the next interval started - this means the display would be constantly powered on despite Waveshare's own warnings against constantly powering on the display. While the manual did not explicitly say that partial refreshing without sleep over a long time would (or would not) cause damage, it did say that partial refreshing should only be done "several" times before a full refresh. Exactly how many is several wasn't stated.

  From 10 repeated testings of the display with the demo, the demo provided's one-second interval partial refresh did not provide good consistent results. Sometimes the interval would be a second, other times slightly shorter or longer, depending on the execution speed of the software. Adding a 3 second delay between intervals also did not provide consistent results.

  For this project, considering the vague guidelines on partial refreshing and its mixed results from the demo, in order to preserve the service life of the ePaper display, it was decided that no partial refresh would be used.

  </p>
</details>

<details>
  <summary>Appendix C</summary>
  <p>Waveshare's manual points out that clearing the display before storage is important. Under "Manual > Overview > Working Principle";

> charged nanoparticles suspended in a liquid migrate under the action of an electric field

Under "Manual > Resources > Datasheet > 2.13inch e-Paper Specification V3 (pdf) > 16. Precautions";

> If the Module is not refreshed every 24 hours, a phenomena known as "Ghosting" or "Image Sticking" may occur. It is recommeded that customers store ... with a completely white image to avoid this issue. 

  </p>
</details>


## Versions
---
Version 1 - first attempt at writing data onto the display. The two black lines divide the width and length into halves.

![v1](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v1.JPG?raw=false "Versions, V1")

Version 2 - noticed that the placement of the CPU usage (a percentage) and the CPU temperature (in Celsius) are placed incorrected on the display in Version 1.

![v2](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v2.JPG?raw=false "Versions, V2")

Version 3 - added timestamp and ip address.

![v3](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v3.JPG?raw=false "Versions, V3")

Version 4 - noticed that running the script at reboot will return an empty string for ip address - the display would show (eg.) ```| 2022-01-13 10:55```. Swapped their placements so that if there's no IP, it can return an empty string without changing the timestamp's placement and also not print an unnecessary "|". 

A thing to note is that the timestamp might also be 'wrong' when first run on reboot, returning time in UTC not localtime. This is caused by the cronjob @reboot running too early before the OS has fetched localtime. There may not be any way to fix this unless systemd is used instead for the reboot's script run because systemd can specify the order in which the script is run.

![v4](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v4_1.JPG?raw=false "Versions, V4")


## Expansions
- Consider designing and 3D-printing a case around the ePaper display + Bonnet.
- Consider adding a 'page 2' with 4 other stats (like Uptime, battery charge (if it had a battery), weather forecast) that alternates getting run
- The Bonnet actually has 2 STEMMA connections (3 pins) and STEMMA QT connections. Perhaps I could add speakers to the Raspberry Pi 400.


## License
---
omgitskuei/RPiDev is licensed under the GNU General Public License v3.0.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 

Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

   [rp400link]: <https://www.raspberrypi.com/products/raspberry-pi-400-unit/>
   [WaveshareEPDlink]: <https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT>
   [Bonnettlink]: <https://www.adafruit.com/product/4862>
   [ePaperRepo]: <https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python>
   [serviceFile]: <https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/cyberdeck_stats_monitor_systemd_unit.service>
   [Apdx]: <https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/README.md#appendix>
