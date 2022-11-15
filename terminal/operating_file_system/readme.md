# Operating the (linux-based) File system
---
Notes on useful terminal commands and what they do

> Author: Omgitskuei
> 
> Last Updated: 2022/11/15
> 
> Status: Active Development


### Commands
A non-exhaustive list of terminal commands I've googled, or found scatter across various guides, tutorials, documentations, tips, etc. This table only contains terminal commands related to the subject shown in the folder name.

Note, if ```apt``` doesn't work, try using ```apt-get```. Older versions of apt use a slightly different command.

---
| Date Added | User request | Command | Description | Tested on |
| ------ | ------ | ------ | ------ | ------ |
| 2022/10/30 | "Print the current working directory." | ```pwd``` | Print current working directory. Eg, entering ```pwd``` in a fresh terminal will show "/home/usrnm" where usrnm is the user name. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Show contents of current directory." | ```ls``` | Print current work directory contents. Note, how results is printed and what defines 'contents' can be customized. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Show contents of current directory, including hidden files." | ```ls -a``` | ```-a``` option abbreviates "all". | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/02 | "List contents of current directory." | ```ls -l``` | This option can be combined with other options - eg. ```ls -al```. The options' order doesn't matter. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/02 | "Show contents of current directory, order by files' modified date." | ```ls -t``` | Results sorted by files' modified date where most recent is first. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Show contents of current director, with results shown as  file paths." | ```ls -d``` | 'File path' as in directories themselves. Eg. "/Document/test.txt" instead of "test.txt" after ```cd /Documents```. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "List contents of current directory, and print author of each item." | ```ls -l --author``` | ... | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "List contents of current directory, but print file sizes in readable formats." | ```ls -hl``` | Readable formats like 1K, 234M, 2G etc. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "List contents of current directory, append a char to indicate type." | ```ls -F``` or ```ls --classify``` | Appended chars include "/" for directory. Indicators: one of "*", "/", "=", ">", "@", "|". | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Show contents of current directory, order by files' size." | ```ls -S``` | Note, it's capital "S". | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/02 | "Show contents of current directory, with the current order reversed." | ```ls --reverse``` | This can be combined with other options, like with ```-t``` for least recent first. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to previous directory." | ```cd -``` | Useful if the previous one isn't a parent or child of the current directory. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to home directory of current user." | ```cd``` | Note, no path provided. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/10/30 | "Change to home directory of a particular user." | ```cd ~[user_name]``` | Note, you may not have permission to write in another user's /home. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/02 | "Determine a file's file type." | ```file [some_file_name].[extension]``` | Note, you may have to type the file extension as well. The output is in this format: ```[file_name].[file_extension]: [file_type]", eg. "rpdiags.txt: ASCII text```. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/02 | "Show the contents of this file." | ```less [some_file_name]``` | Works with txt, config files, and scripts. Use ```[CTRL] + [z]``` to exit the document viewer. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Copy this file to this new location." | ```cp [directory of the file you want to copy] [directory where to paste the file]``` | Note that specifying the file extension is important. Note, you might need to 'sudo' depending on where to paste. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Rename/Move the directory/file." | ```mv [???] [???]``` | Can also overwrite files (by accident too). | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Create directories." | ```mkdir [some file]``` | This command can be chained, with ' [some file]' this part repeating. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "." | ```rm [???]``` | Remove. | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Create hard/symbolic links." | ```ln [???]``` | . | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Create directories." | ```mkdir [???]``` | ... | Raspberry Pi OS, based on Debian (Bullseye) |
| 2022/11/15 | "Create directories." | ```mkdir [???]``` | ... | Raspberry Pi OS, based on Debian (Bullseye) |


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
- Linux OS doesn't rely on file extensions (eg, .txt) to determine file type or purpose, so Linux users can name files any way they want. That said, some apps and packages do defer to file extensions.
- Do not use spaces when naming files. This makes accessing these files via terminal difficult.

##### More on less when viewing file contents
The program less was designed to replace the program more, which could only read forward, not backwards, and is a wordplay on the saying "less is more".
less is a part of a class of programs called "pagers".
Pagers are for viewing long text documents in 'page' form.

As practice, try doing ```less``` to some files:
1. ```cd``` and ```ls -la``` to the file
2. ```file [some file]``` to show file type (can certain file types like JPG be viewed by ```less```?)
3. ```less [some file]```

| Controls | Description |
| ------ | ------ |
| ```b``` | Back one page |
| ```spc``` | Forward one page |
| ```Up arrow key``` | Up one line |
| ```Down arrow key``` | Down one line |
| ```G``` | Go to end of file |
| ```g``` | Go to beginning of file |
| ```/[some text]``` | Search *foward* for the next instance of some text |
| ```n``` | Search next occurence of previous search |
| ```h``` | Display help |
| ```q``` | Quit the file viewer and return to terminal |

##### Directories of interest
| Directory | Notes |
| ```/bin``` | Programs needed for system boot, usually executables |
| ```/boot``` | Programs needed by the terminal for boot loader, or boot time drivers |
| ```/boot/vmlinuz``` | The linux kernel might be located here |
| ```/dev``` | Contains device nodes, kernel maintains a list of all devices it understands |
| ```/etc``` | contains config files, system service boot-time shell scripts |
| ```/etc/crontab``` | File defining when to run automated jobs |
| ```/etc/fstab``` | Table of storage devices and their mount points |
| ```/etc/passwd``` | User accounts |
| ```/home``` | Each user given a dir in home, ordinary users can only write files to their own directory inside their home |
| ```/lib``` | Core system programs' shared library files |
| ```/lost+found``` | Used in case of corruption |
| ```/media``` | Usually, the default mount point for removable media (CD, USB, etc) |
| ```/mnt``` | Mount point for removeable devices mounted manually |
| ```/opt``` | Directory for installing optional/commercial software |
| ```/proc``` | A virtual file system maintained by Linux kernel, allowing users to read logs on the Kernel itself |
| ```/root``` | root account's home directory |
| ```/sbm``` | "System Binaries" |
| ```/tmp``` | A location for transient files, some config to automatically empty after each boot |
| ```/usr``` | Contains all programs & support files used by regular users |
| ```/usr/bin``` | Executable programs installed by Linux distribution |
| ```/usr/sbin``` | Contains more sys admin programs |
| ```/usr/lib``` | Shared libraries for ```/usr/bin``` |
| ```/usr/local``` | Programs not included with distro but intended for system-wide use |
| ```/usr/share``` | Contains shared data icons, sound files, config, etc, for ```/usr/bin``` |
| ```/usr/share/doc``` | Most packages will include documentation in this directory, sort by package name |
| ```/var``` | Directory for 'relatively more likely to change' data, eg. database, user email storage |
| ```/var/log``` | logs for system activity, may need su/sudo to read the files |
| ```/usr/log/messages``` | ^ Same as above |

##### More on ls
- When user calls ```apt``` to install packages and their dependencies, under the hood, ```apt``` calls ```dpkg``` to do the installing.
- apt can search online package repositories for information about packages (maintainer, description, dependencies, etc), while dpkg is local only.
- apt can download packages and their dependencies, while dpkg cannot.
- apt will install dependencies needed by a package automatically when the user install that package, while dpkg will not handle dependencies for the user.

##### Symbolic link/Soft link/Symlink
- Program requiring a shared resource referencing it with symlink s. that version changes don't require changing anything else besides directory of symbolic links. "lib 2 -> lib 2.7" - "lib 2" is the name of symlink and "lib 2.7" is the actual resource name.

##### Terminal vs. GUI
- Commands used in cmd might not always save time compared to using GUI especially drag-drop operations compared to typing out cp or mv commands. However, Terminal still has uses - complex combinations of cmds or specific use of options lead to fast and precise results - eg. copy all html files that don't already exist in a directory, and also overwrite existing files if the existing file is an older version like this; ```cp -u *.html destination```.
- Most of the power of terminal comes from Wildcards like:
-- ```*``` (any char), 
-- ```[characters]``` (any char from the set 'characters'), 
-- ```[alnum``` (alphanumeric is alpha and digits - any uppercase or lowercase letters or any decimal digits), 
-- ```[:alpha:]``` (alphabetic - uppercase and lowercase letters), 
-- ```[:digit:]``` (numbers),
-- ```[:upper:]``` (lower char),
-- ```[:lower:]``` (upper char),
-- ```g*``` (all files starting with 'g'),
-- ```b*.txt``` (all txt files beginning with 'b'),
-- ```[abc]*``` (any file beginning with either a, b, c),
-- ```AB[0-9][0-9]``` (AB followed by 2 numbers each between 0 and 9),
-- ```[[:upper:]]*``` (file beginning with one upper character),
-- ```[![:digit:]]*``` (files not beginning with a number),
-- ```*[[:lower:]123]``` (files ending with a lowercase letter or 1,2,3)



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
