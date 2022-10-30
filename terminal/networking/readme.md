# Networking
---
Notes on useful terminal commands and what they do

> Author: Omgitskuei
> 
> Last Updated: 2022/10/30
> 
> Status: Active Development

### Commands
A non-exhaustive list of terminal commands I've googled, or found scatter across various guides, tutorials, documentations, tips, etc. This table only contains terminal commands related to the subject shown in the folder name.

Note, if ```apt``` doesn't work, try using ```apt-get```. Older versions of apt use a slightly different command.

---
| Date Added | User request | Command | Description | Tested on |
| ------ | ------ | ------ | ------ | ------ |
| 2022/09/20 | "List all available wifi, please." | ```sudo iwlist wlan0 scan``` | List all wireless networks detected by wifi, and their details. Can be verbose. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/20 | "List all available wifi, please." | ```sudo iwlist wlan0 scan \| grep -e ESSID -e Address -e Quality -e Encryption ``` | List all wireless networks detected by wifi, specifically showing each result's ESSID, Address, Quality, and Encryption only. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/20 | "Show statistics on my current wifi connection." | ```iwconfig wlan0``` | Shows ESSID, Access point, Frequency, Bit Rate, Quality, Signal level, Missed beacons, etc. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/20 | "Show my wifi's IP address." | ```ifconfig wlan0```, ```ifconfig wlan0 \| grep inet``` | Same as above, but only show lines with "inet". | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Show my wifi's IP address." | ```hostname -I``` | Show self IP address. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Search iperf3 with apt to see if this distribution has iperf3." | ```apt-cache search iperf3``` | Search for iperf3, a comprehensive and flexible tool for testing network bandwidth. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Install iperf3, please." | ```sudo apt install iperf3 -y``` | Install iperf3. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Start a server on localhost for bandwidth speed test. | ```iperf3 -s``` | Start a server on current machine listening on Port 5201. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Connect to localhost server and run bandwidth test." | ```iperf3 -c 127.0.0.1``` | Open a NEW TERMINAL - keep the terminal with the localhost server open. Start bandwidth speed test. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Connect to localhost server and run bandwidth test." | ```iperf3 -c 127.0.0.1 -J``` | Same as above, add ```-J``` option at the end to return results as a JSON for scripts. | Raspberry Pi OS, based on Debian (Bullseye) |

### Running the program
---
Open the terminal on your linux system and type the command into the terminal, and press Enter.
