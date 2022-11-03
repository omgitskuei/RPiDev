# Terminal
---
Notes on useful terminal commands and what they do

> Author: Omgitskuei
> 
> Last Updated: 2022/11/02
> 
> Status: Active Development

### Commands
A non-exhaustive list of terminal commands I've googled, or found scatter across various guides, tutorials, documentations, tips, etc. This table only contains terminal commands related to the subject shown in the folder name.

---
| Date Added | User request | Command | Description | Tested on |
| 2022/10/30 | "Open virtual terminal." | ```[CTRL] + [ALT] + [F1-F6]``` | Terminals run behind the GUI, access virtual terminals 1 to 6 with [F1] to [F6]. Switch between with [CTRL] + [ALT] + [F#]. [CLTR] + [ALT] + [F7] to return to desktop. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/10/30 | "Clear the terminal." | ```clear``` | Note, this only remove previous commands and output - it doesn't reset working directory to /home nor stop processes started by this terminal. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |
| 2022/10/30 | "Close terminal" | ```exit``` | Closes the terminal. | Raspberry Pi 400, Raspbian (Debian, Bullseye) |

| 2022/11/02 | "" | `````` | . | Raspberry Pi 400, Raspbian (Debian, Bullseye) |


### Running the program
---
Open the terminal emulator on your linux system and type the command into the terminal, and press Enter.


### Notes
- The syntax for writing linux commands is ```[cmd] -[options] --[long_option] [args]```
-- eg. ```ls -l --all``` is the same as ```ls -la```
-- eg. ```ls -la --reverse```
- Dragging to highlight, then left-clicking the highlighted text will copy it (like doing [CTRL] + [c])
- Clicking the mouse wheel or middle mouse button will paste (like doing [CTRL] + [v])
