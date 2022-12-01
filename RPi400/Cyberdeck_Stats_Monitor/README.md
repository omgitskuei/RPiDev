# Cyberdeck Stats Monitor for the Raspberry Pi 400

![titlepic](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v4.JPG?raw=false "Title image")

This Raspberry Pi 400 project displays ...
- CPU usage %, 
- RAM usage %, 
- Disk space used %, 
- CPU temperature, 
- machine ip address, 
- and timestamp 

... on a Waveshare ePaper (250 x 122 pixels, 2.13 inch EPD HAT for Raspberry Pi, Black/White, RPI SPI interface) connected to a Adafruit Cyberdeck Bonnett (which then connects to the Raspberry Pi 400's GPIO pins).
The scripts clear.py (clears the display) and update.py (gets and writes data onto the display) are written in python.


## Limitations

- This project has not been tested on other Raspberry Pi models besides Raspberry Pi 400, but if the OS is Raspberry Pi OS (Bullseye) then it should work.
- The update.py python script relies on os.popen() which **might** make it compatible with Linux systems only.
- This project has not been tested with other Waveshare ePaper displays - though changing the library for the correct corresponding one should enable them to work.
- This project uses the gpio python library so attempting to run it on a non-raspberry pi system will throw errors.


## To Do List

- 3D print the case that will house the ePaper and Bonnet, sand and spray paint the case, and slot it over the components.
- Add a stdout/stderr to all systemd jobs.
- Add GPIO sensing Pin 17 GRD as input, to determine if the project is plugged in or not.


## Expansion

- Consider adding a 'page 2' of stats, like Uptime, battery charge (if it had a battery), weather forecast.
- The Bonnet actually has 2 STEMMA connections (3 pins) and STEMMA QT connections. Perhaps I could add speakers to the Raspberry Pi 400.


## Tutorial

### _Components_

| Component name | Description | Link | Importance |
| ------ | ------ | ------ | ------ |
| Raspberry Pi 400 | A Raspberry Pi computer with a quad-core 64-bit processor, 4GB of RAM, wireless networking, dual-display output, and 4K video playback, as well as a 40-pin GPIO header. | [Raspberry Pi 400][rp400link] | Necessary |
| Waveshare ePaper 2.13 inch Black/White display HAT | Note there's multiple two-colored 2.13" ePaper displays from Waveshare - the component used here does not have the "(B)", "(C)", or "(D)" in its name. | [Waveshare ePaper 2.13" HAT][WaveshareEPDlink] | Necessary |
| Adafruit Cyberdeck Bonnett | It's a plug-and-play HAT attached to the GPIO pins. For the Raspberry Pi 400, it attaches at a slant with the HAT's pins facing the user. It's called a 'bonnett' because it's about half the size of a regular HAT. | [Adafruit Cyberdeck Bonnett][Bonnettlink] | Necessary |
| 3D Printed Case | Take the STL file to a 3D printing shop, could be ~15 USD for the case. Afterwards, have a file ready to remove any extra bits. | n/a | Optional |


### _Instructions_

<details>
  <summary>Step 1 - Acquire the necessary components and connect them</summary>
  <p>Put the Adafruit Cyberdeck Bonnet (aka 'Bonnet') flat on the table such that the GPIO pins are facing upward and the slanted GPIO sockets are below the GPIO pins.

Plug the Waveshare ePaper 2.13" display HAT (aka 'ePaper') into the Bonnet's GPIO pins such that the ePaper's orange tape ( with white text "FPC-7528B" printed on it) is to the left and the display is facing up.

Plug the Bonnet's slanted GPIO socket into the Raspberry Pi 400's (aka 'Pi') GPIO pins such that the ePaper's display is facing the keyboard user.

Your components should be connected like shown in the photo. Unlike the photo, your ePaper should currently be a blank white. The photo is showing my Programmer handle OmgItsKuei by running a script that draws a black rectangle and writing in white over the rectangle. This script was used to practice using the Waveshare ePaper python library.
![guidepic1](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic1.JPG?raw=false "Guide, Step 1")
  </p>
</details>


<details>
  <summary>Step 2 - Make sure Python 3 is installed</summary>
  <p>Python 3 is already installed on the Raspberry Pi 400 with Raspberry Pi OS (Bullseye).

If you're not sure if Python 3 is installed, open terminal and try:

```Linux Kernel Module
python3
```

The terminal should output the python version number.

If you don't have python3, go download and install it from the python website or use apt.
		
```Linux Kernel Module
sudo apt install python3
```

![guidepic2](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic2.JPG?raw=false "Guide, Step 2")        
  </p>
</details>


<details>
  <summary>Step 3 - Make sure the ePaper driver is in the ./library directory</summary>
  <p>Download the RPiDev repository to get the folder `Cyberdeck_Stats_Monitor`.

I recommend saving the repo RPiDev in /home/yourUser/. Later commands use that directory as an example. If you save it elsewhere, don't forget to modify commands to the custom directory.

![guidepic3](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic3.JPG?raw=false "Guide, Step 3")

:heavy_exclamation_mark:  The file structure of the folder `Cyberdeck_Stats_Monitor` must remain unchanged. 
			
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
  <summary>Step 4 - Add Cron jobs to run clear.py on reboot (startup and restart) and update.py every 5 mins</summary>
  <p>Start the Linux terminal and input this command to start adding cron jobs.
		
```Linux Kernel Module
crontab -e
```

You'll see something like this picture. Add the missing white text.

![guidepic4](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic4.png?raw=false "Guide, Step 4")

```Linux Kernel Module
@reboot /home/yourUser/omgitskuei/RPiDev/RPi400/Cyberdeck_Stats_Monitor/python/clear.py > /home/yourUser/Documents/logs/cyberdeck_reboot_clear.log 2>&1
```

For easy debugging, I recommend adding the command to explicitly send the job's output to a log file by adding ```> [path] [STDOUT, STDERR, both]``` to the end of each job. The ```2>&1``` means writing both writing job output and job errors to the same log file. Note, you can use ```>>``` if you want to append contents to the log files instead of overwrite the log files.
    
- Add a crontab job to run the ```clear.py``` script on reboot (reboot startup as well as restart) - requires Linux system to use crontab. To get this step to work on Windows/Mac, an equivalent to the crontab program is needed. 
- Then, add a crontab job to run the ```cyberdeck_stats_monitor.py``` script immediately on startup. This is because a repeating crontab job does not run until its interval has elapsed at least once. Without doing this step, the display would not start until 5 minutes after startup.
- Lastly, add a crontab job to run the cyberdeck_stats_monitor.py script every 5 minutes. This interval can be modified to the user's liking. That said, Waveshare recommends refresh intervals between 3 minutes and 24 hours. :heavy_exclamation_mark: [See Appendix B for details and other precautions][Apdx]. If you want to execute the ```cyberdeck_stats_monitor.py``` script just once, the 'meat' of cyberdeck_stats_monitor.py needs to be wrapped in a loop so it stays running after executing it once - if you're doing this, pay attention to the Appendix B on how to implement ePaper. 
  </p>
</details>


<details>
  <summary>Step 5 - Use systemd to run clear.py script before shutdown</summary>
  <p>
Add the systemd unit file cyberdeck_stats_monitor_systemd_unit.service configured to run the clear.py script right before shutdown - requires Linux system to use systemd.

For other OS, you need an alternative to systemd to run the clear.py before shutdown. 

:heavy_exclamation_mark: See Appendix C for why we're running the clear.py script before every shutdown. It goes into [proper storage][Apdx] for the ePaper. 
		
Start the Linux terminal emulator and input 

```Linux Kernel Module
sudo cp [wherever you saved this folder]/Cyberdeck_Stats_Monitor/cyberdeck_stats_monitor_systemd_unit.service. /etc/systemd/system
```

Ignore the ```scrot``` commands - they're for taking this screenshot.

:heavy_exclamation_mark: The .service file shown in the screenshot is missing the [Install] config - see the file's contents [here][serviceFile] for the missing [Install] config.

![guidepic5](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic5_1.png?raw=false "Guide, Step 5")

Refresh the systemd configuration files by entering this command into terminal.

```Linux Kernel Module
sudo systemctl daemon-reload
```
  </p>
</details>


<details>
  <summary>Step 6 - Enable the cyberdeck_stats_monitor_systemd_unit.service in /etc/systemd/system so that it runs at the next boot</summary>
  <p>Open the Linux terminal emulator and input systemctl enable cyberdeck_stats_monitor_systemd_unit.

![guidepic7](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic7_1.png?raw=false "Guide, Step 7")
  </p>
</details>


<details>
  <summary>Step 7 - Try running the scripts through terminal</summary>
  <p>Try running the update.py script throught terminal with cd and python3.

```Linux Kernel Module
cd omgitskuei/RPiDev/RPi400/Cyberdeck_Stats_Monitor/python
python3 update.py
```

You should see something similar to the image below.

![guidepic6](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/guidepic8.JPG?raw=false "Guide, Step 8")

If this failed, its likely because the SPI Interface is currently disabled. Use raspi-config to enable the SPI Interface.

```Linux Kernel Module
sudo raspi-config
```

This will open the Raspberry Pi Configuration application. Choose Interfacing Options -> SPI -> Yes Enable SPI interface.
  </p>
</details>


### _Appendix_

<details>
  <summary>Appendix A</summary>
  <p>The python scripts clear.py and update.py rely a specific file structure to import Waveshare ePaper display's library and to read essential bmp files.
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


## Change Logs

Version 1 - first attempt at writing data onto the display. The two black lines divide the width and length into halves.
![v1](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v1.JPG?raw=false "Versions, V1")

Version 2 - noticed that the placement of the CPU usage (a percentage) and the CPU temperature (in Celsius) are placed incorrected on the display in Version 1.
![v2](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v2.JPG?raw=false "Versions, V2")

Version 3 - added timestamp and ip address.
![v3](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v3.JPG?raw=false "Versions, V3")

Version 4 - noticed that running the script at reboot will return an empty string for ip address - the display would show (eg.) ```| 2022-01-13 10:55```. Swapped their placements so that if there's no IP, it can return an empty string without changing the timestamp's placement and also not print an unnecessary "|". A thing to note is that the timestamp might also be 'wrong' when first run on reboot, returning time in UTC not localtime. This is caused by the cronjob @reboot running too early before the OS has fetched localtime. There may not be any way to fix this unless systemd is used instead of cron for the reboot's script run because systemd can specify the order in which the script is run whereas cron can't specify order.
![v4](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v4_1.JPG?raw=false "Versions, V4")

Version 5 - added configparser to read ini file - the ini file can modify the display to show Farenheit instead of Celsius (default) and can also disable the display being refreshed. Noticed this version breaks the cron job due to Permission Denied when trying to read the ini file.
![v5](https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/pic/photos/v5.JPG?raw=false "Versions, V5")

Version 6 - replaced cron jobs with systemd instead, debugged Permission denied when trying to read ini file, debugged systemd unit file shutdown service causing shutdown to hang when display is not plugged in by removing unit "Requires=".

## License

omgitskuei/RPiDev is licensed under the GNU General Public License v3.0.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 

Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

   [rp400link]: <https://www.raspberrypi.com/products/raspberry-pi-400-unit/>
   [WaveshareEPDlink]: <https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT>
   [Bonnettlink]: <https://www.adafruit.com/product/4862>
   [ePaperLiblink]: <https://github.com/omgitskuei/RPiDev/tree/main/RPi400/Cyberdeck_Stats_Monitor/library/waveshare_epd>
   [ePaperRepo]: <https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python>
   [serviceFile]: <https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/cyberdeck_stats_monitor_systemd_unit.service>
   [Apdx]: <https://github.com/omgitskuei/RPiDev/blob/main/RPi400/Cyberdeck_Stats_Monitor/README.md#appendix>
