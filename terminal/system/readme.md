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
| 2022/10/30 | "Print disk usages" | ```df``` | Displays Filesystems like /dev/root, current total, used free capacity in KB, along with mount points. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/09/20 | "Print disks info, please." | ```sudo fdisk -l``` | Lists size, type, etc.. information on all disks (wordy). | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Print OS info." | ```cat /etc/*-release``` | Displays OS info; OS name, Version (ID, Codename), home-url, bug-report-url. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/10/30 | "Print current date." | ```date``` | Displays system's current date in format "DOW DOM MON YYYY HH:MM:SS AM/PM 'CST'". Note, CST timezone is always displayed, CST is the wrong timezone for Taiwan but changing Raspberry Pi Configuration -> Localization settings has no affect. Also, format changes based on Localization settings. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/10/30 | "Display RAM/memory usage." | ```free``` | Displays total, used, free, available RAM in KB. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/11/03 | "Show all installed systemd units" | ```systemctl list-unit-files``` | . | Raspberry Pi 400, Raspbian (Debian, Bullseye) |

| 2022/10/30 | "" | `````` | . | Raspberry Pi 400, Raspbian (Debian, Bullseye) |



### Running the program
---
Open the terminal emulator on your linux system and type the command into the terminal, and press Enter.


### Notes


##### Difference between running a terminal emulator and working with a virtual terminal
- Diff1
- Diff2
- Diff3
