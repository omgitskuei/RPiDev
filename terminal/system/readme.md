# Getting System and Hardware info
---
Notes on useful terminal commands and what they do

> Author: Omgitskuei
> 
> Last Updated: 2022/10/30
> 
> Status: Active Development

### Commands
A non-exhaustive list of terminal commands I've googled, or found scatter across various guides, tutorials, documentations, tips, etc. This table only contains terminal commands related to the subject shown in the folder name.

---
| Date Added | User request | Command | Description | Tested on |
| ------ | ------ | ------ | ------ | ------ |
| 2022/09/04 | "Print GPIO info." | ```pinout``` | Displays the hardware info; GPIO40 pins, ram, storage type, USBs, SoC, etc.. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/20 | "Print disks info, please." | ```sudo fdisk -l``` | Lists size, type, etc.. information on all disks (wordy). | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Print OS info." | ```cat /etc/*-release``` | Displays OS info; OS name, Version (ID, Codename), home-url, bug-report-url. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |

### Running the program
---
Open the terminal on your linux system and type the command into the terminal, and press Enter.
