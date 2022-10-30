# Administrating Packages
---
Notes on useful terminal commands and what they do

> Author: Omgitskuei
> 
> Last Updated: 2022/09/19
> 
> Status: Active Development

### Commands
A non-exhaustive list of terminal commands I've googled, or found scatter across various guides, tutorials, documentations, tips, etc. This table only contains terminal commands related to the subject shown in the folder name.

Note, if ```apt``` doesn't work, try using ```apt-get```. Older versions of apt use a slightly different command.

---
| Date Added | User request | Command | Description | Tested on |
| ------ | ------ | ------ | ------ | ------ |
| 2022/09/04 | "Install a package called ```rpi-imager```, please?" | ```sudo apt install rpi-imager``` | Installs the "RPI Imager" program, which is used to create SD card images of Raspberry Pi OS's. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Do my packages have updates?" | ```sudo apt update``` | Lists info on upgrades for all packages that can be updated. Note, this doesn't install the updates. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/19 | "List all local packages on this machine" | ```dpkg --list``` | dpkg only indexes local packages - Lists all local pacakges | NOT YET TESTED |
| 2022/09/19 | "List all local installed packages on this machine" | ```apt list --installed``` | Lists all local pacakges that are installed, do NOT forget the flag otherwise all packages listed anywhere (even on remote online repositories) will be listed. | NOT YET TESTED |
| 2022/09/10 | "What are all these packages that can be updated?" | ```apt list --upgradable``` | Lists info on packages that can be updated. Note, this doesn't install the updates. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "What's my current disk space?" | ```df -h``` | Display all filesystems' total size, used, avail, used%, path. NOTE, apt will NOT check if disk space is sufficient for an install or upgrade. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Delete archived packages to free disk space, please?" | ```sudo apt clean``` | All downloaded packages (.deb) are kept in /apt/archive, can be deleted to free disk space | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Install all updates for all packages with available upgrades, please?" | ```sudo apt full-upgrade``` | Download and install all updates for all upgradable packages, some will be deprecated and archived. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Delete deprecated packages, please?" | ```sudo apt autoremove``` | Delete all deprecated packages. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Search for 'locomotive'-related packages." | ```apt-cache search locomotive``` | Searches package repos like packages.ubuntu.com for public info on packages. No changes made so ```sudo``` not needed. Eg. Keyword 'locomotive' used. One of the results will be a package called "sl" (abbr. "steam locomotive"). | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Show me details on this package ```sl``` | ```apt-cache show sl``` | Display details about the package before/after installing a package. Note, you can click on URL hyperlinks inside Terminal with Alt + Left Click. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Install a package called ```sl```, please?" | ```sudo apt install sl``` | Linux users using terminal to navigate folder trees will be using the command ```ls``` a lot. When "sl" typos happen, terminal will run ```sl``` and display a textart train running across the terminal instead of a linux error message about no recognized "sl" command. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Run this package called ```sl```." | ```sl```, ```sl -F```, ```sl -a```, ```sl -l```, ```sl -c``` | Packages can usually take 'flags'. sl takes '-F' (case-sensitive), '-a', '-l', and '-c' flags. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Uninstall a package called ```sl```, please?." | ```sudo apt remove sl``` | Uninstalls the package but leaves its config files, if any. Will confirm with user unless given the ```-y``` flag | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/09/04 | "Uninstall a package called sl, and also delete all the package's config files, please?" | ```sudo apt purge sl``` | Uninstalls the package and delete its config files. | Raspberry Pi OS, based on Debian (Bullseye) |

### Running the program
---
Open the terminal on your linux system and type the command into the terminal, and press Enter.

### Notes
---
##### Difference between apt and dpkg
- When user calls ```apt``` to install packages and their dependencies, under the hood, ```apt``` calls ```dpkg``` to do the installing.
- apt can search online package repositories for information about packages (maintainer, description, dependencies, etc), while dpkg is local only.
- apt can download packages and their dependencies, while dpkg cannot.
- apt will install dependencies needed by a package automatically when the user install that package, while dpkg will not handle dependencies for the user.

| Common Use cases | Supported by ```apt``` | Supported by ```dpkg``` |
| ------ | ------ | ------ |
| List all currently installed packages | YES | YES |
| Search online for packages to install by keywords | YES | NO |
| Look up details about a specific package | YES | NO |
| Download a package | YES | NO |
| Download a package's dependencies | YES | NO |
| List all currently downloaded but not installed packages | ??? | YES |
| Install a package (or a package, that's another package's dependency) | YES | YES |
| Remove (uninstall, keep configs) a package | YES | YES |
| Purge (uninstall, delete configs) a package | YES | YES |

Comparatively, ```apt``` is more user friendly than ```dpkg``` since it will automatically handle things like searching repositories and also downloading dependencies.
Despite that, ```dpkg``` is still relevant because its use of flags called "package states" will keep track of all packages' current progress in the installation cycle;
Package states:
| Package states | Description |
| ------ | ------ |
| ```not-installed``` | The package is not installed on your system. |
| ```config-files``` | Only the configuration files of the package exist on the system. |
| ```half-installed``` | The installation of the package has been started, but not completed for some reason. |
| ```unpacked``` | The package is unpacked, but not configured. |
| ```half-configured``` | The package is unpacked and configuration has been started, but not yet completed for some reason.. |
| ```triggers-awaited``` | The package awaits trigger processing by another package. |
| ```triggers-pending``` | The package has been triggered. |
| ```installed``` | Installation successful and complete. |

If an installation is halted, or fails, these states will help with debugging. But generally, the installation process should be successful, and so this level of detail all the time would probably be unnecessarily verbose.
