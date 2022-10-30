# Operating the (linux-based) File system
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
| 2022/10/30 | "Print the current working directory." | ```pwd``` | Print current working directory. Eg, entering ```pwd``` in a fresh terminal will show "/home/usrnm" where usrnm is the user name. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Show me what's in the current working directory." | ```ls``` | Print current work directory contents. Note, how results is printed and what defines 'contents' can be customized. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Show what's in the current directory (including hidden files)." | ```ls -a``` | ```-a``` option abbreviates "all". | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to previous directory." | ```cd -``` | Useful if the previous one isn't a parent or child of the current directory. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to home directory of current user." | ```cd``` | Note, no path provided. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to home directory of a particular user." | ```cd ~username``` | Note, you may not have permission to write in another user's /home. | Raspberry Pi OS, based on Debian (Bullseye) |


### Running the program
---
Open the terminal on your linux system and type the command into the terminal, and press Enter.


### Notes
---
##### More on linux file systems
- "Directory" and "Folder" are used interchangeably.
- The first folder (that contains all other folders) is the "root". This means linux systems have one single file system. The file system GUI shows this singular tree upended with root at the top.
- Directory of root is nothingness/a space/"". So the system's users folder "usr" is in "/usr" - that space/nothing in front of the slash "/" is root. Root isn't actually spent out. 
- Linux file systems is a hierarchical system where "everything is a file", including folders. In Linux, there's no difference between a file and a directory.
- For detachable storages like USBs, they're each 'mounted' at some point in the file system tree.
- Each user is given their own /home directory. When that user starts a new terminal session, the terminal starts them at their /home.
- In scripts, try to write relative paths instead of absolute paths.
- "username@raspberrypi:~/Documents" might be displayed on the terminal. The "~" means the /home of a user. This dir points to the Documents folder in their /home.
- If you typed ```pwd``` at "username@raspberrypi:~/Documents", it'll say "/home/username/Documents".
- If you ```cd``` to root and typed ```pwd```, it'll print "/".
- There are special symbols for using file systems; "." means working/current directory. ".." means parent directory. Note, in almost all cases, the "." current directory can be omitted.
- 


##### More on ls
- When user calls ```apt``` to install packages and their dependencies, under the hood, ```apt``` calls ```dpkg``` to do the installing.
- apt can search online package repositories for information about packages (maintainer, description, dependencies, etc), while dpkg is local only.
- apt can download packages and their dependencies, while dpkg cannot.
- apt will install dependencies needed by a package automatically when the user install that package, while dpkg will not handle dependencies for the user.











### Work in progress... ###

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
