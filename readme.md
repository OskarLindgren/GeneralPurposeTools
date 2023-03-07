# General Purpose Tools

#### GPT was made with
Love & Code by Oskar Lindgren

-----

## How to use
Run commands by selecting them in the program or typing GPT <COMMAND> <ARGS> in your terminal

| **COMMAND**                                | **ARGS**                                                               | **DESCRIPTION**                                   |
| -----------------------------------------: | :--------------------------------------------------------------------- | :------------------------------------------------ |
|                                `help`, `h` |                                                                        | Displays commands and options                     |
|                             `version`, `v` |                                                                        | Displays program version                          |
|                                    `sinfo` |                                                                        | Displays system information                       |
|                                  `whereis` | FILENAME DRIVE IGNORESYSFILES *( y \| n )*                             | Finds path(s) to file searched for                |
|                       `calculator`, `calc` |                                                                        | Opens a simple calculator                         |
|               `activate_windows`, `ActWin` |                                                                        | Activates windows using black magic               |
|        `speed_test`, `test_speed`, `speed` | DRIVE SIZE(MB)                                                         | Tests the speed of a drive                        |
|       `port_scanner`, `scan_port`, `pscan` | IP PORT *( single \| range \| * \| / )*                                | Scan open ports on a given ip adress              |
| `display_dir`, `print_dir`, `ddir`, `pdir` | DIR MODE *( folders or 1 \| files or 2 \| show_hidden or 3)* OUTPUTDIR | Make a .txt with a formated view of the directory |

-----

## Installation 

### 📦・Manually compiling GPT
1. Start off by installing [python](https://www.python.org/) 🐍
2. Run `setup.bat`
3. `GPT.exe` will now be located in `./output`

**or**

1. Start off by installing [python](https://www.python.org/) 🐍
2. Open your terminal
3. Navigate to the directory where you have the source code
4. Run `pip install -r requierments.txt` *or* run `pip install <module>` for every module in `requierments.txt`
5. Run `pyinstaller --noconfirm --onefile --console --icon "NONE" --name "GPT" --add-data "./functions;functions/" --add-data "./main.ini;." "./main.py"`\*
6. Wait... 💤
7. Delete the folder called `build` and the file called `GPT.spec`\*\*
8. `GPT.exe` will now be located in `./output`
9. Give yourself a well deserved pat on the back. You just compiled a python program! 🎉


\* *(Feel free to mess around with the params for the `pyinstaller` call. Altough `--onefile` and `--console` are needed for GPT to function)* 

\*\* *(If you changed the `--name` param then the `.spec` file will have a diffrent name)*



### 🖥️・Being able to run it from your terminal
1. Open your windows search bar and type `Edit the system environment variables`
2. Click on `Enviroment Variables...` in the bottom right corner
3. On the lower half of the window scroll down untill you see `Path` on the left side of the table
4. Double Click `Path`
5. Place `GPT.exe` in one of those folders **or** Place `GPT.exe` wherever you want, then add that directory to Path by clicking `New` in the top right corner of the window\*
6. Open your terminal an run `gpt`, `GPT`, `gpt.exe` or `GPT.exe`

\* *(Don't place `GPT.exe` inside of `C:\windows\system32`. It's bad practise and can lead to problems down the line)*

-----

## Info
GPT a.k.a General Purpose Tools is a free open source command line program licensed under a `BSD 3 License`.

GPT is designed to help you with your every day computing needs!

GPT is written in only python.

GPT is build in- and tested on windows machines. Unix support is thus not officially supported. *(That's not to say that it's completly broken)*


*You are free to edit the code as you see fit. But if you redistribute it, do not lock it behind a paywall as per the license and make sure to add yourself to the list of authors in `main.ini` :)*

*V 1.0 - 1.2 can be found at [MageSneaky's github](https://github.com/MageSneaky/CatTools) under the name `CatTools`*

*V1.3 is lost to time :(*
