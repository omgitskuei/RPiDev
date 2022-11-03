# RPiDev
---
This repo is a Collection of notes on using the terminal as well as an archive of my Raspberry Pi projects, sorted by Raspberry Pi model.
Rasberry Pi projects are sorted by model here because I found online resources a bit overwhelming to sift through when starting out.
Often times, I would click on a fun project online only to find out that it uses a Raspberry Pi Pico or Raspberry Pi 4 Model B instead.
There's no doubt some of those projects are transferable across models, but it's work intensive to have to dive into the code or hardware to figure out compatibility.
By sorting projects by model, I might copy a project from one model's folder into another model's then change the software to work with a different model.

The contents of this repo are grouped by topic. A readme (.md file) is used to display a table of terminal commands. The table will include date tested on particular hardware, command, description of its use, There may be some overlap in the notes across topics because they may use the same commands here and there. Eg. It's possible to see the "apt-cache search keyword" (look up packages by keyword) appear in other terminal commands notes besides the readme on administrating (Install, Run, Update, Uninstall) packages.

### Limitations
---
Here, notes are tested on Raspberry Pi 400. The distro used by the model will be in the readme - note that commands that also work on older systems may have small differences in syntax between the notes and actual results if ran elsewhere (Eg. a non-Debian distro).

### Table of Contents
---
### _Terminal_
| Link | Description |
| ------ | ------ |
| [RPi400][rpi400] | Raspberry Pi 400 Projects
| [Administrating Packages][terminalAdminPackages] | How to install, run, update, and uninstall packages. |
| [System OS, Hardware][terminalSys] | How to look up system OS info. |
| [File system Operations][terminalFileOps] | How to use command line to operate file systems. |

### _Remote Access_
WIP

### License
---
omgitskuei/LinuxDev is licensed under the GNU General Public License v3.0.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 

Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

   [terminalAdminPackages]: <https://github.com/omgitskuei/RPiDev/tree/main/terminal/administrating_packages>
   [terminalSys]: <https://github.com/omgitskuei/RPiDev/tree/main/terminal/system>
   [terminalFileOps]: <https://github.com/omgitskuei/RPiDev/tree/main/terminal/operating_file_system>
   [rpi400]: <https://github.com/omgitskuei/RPiDev/tree/main/RPi400>
   
