# v1.0 Patchnotes:

*We uhhh... made the program?*

-----

# v1.1 Patchnotes:

### Fixed formating issues
> Added `%` to percentage based values

-----

# v1.2 Patchnotes:

### Added a calculator function
> Adds the ability to perform simple arithmatic such as 1+2 or 69**420/1337
### Made changes changes to sinfo
> Fixed sinfo saying that you are using AMD64 regardles or architecture
> Added GPU info *(WIP)*
### Made changes to the help command
> Made more clear
> Changed how the authors are worked internaly (making it easier to add more authors)

-----

# v1.3 Patchnotes: 

### Changed networking information
> Added external  ipv4 adress
> Changed `ip adress` to `internal ipv4 adress`
### Changed `Press enter to continue` to `Press enter to continue...`

-----

# v1.4 Patchnotes:

### Completly rewrote the program
> Functions are now imports making for a much cleaner code
### Rewrote the whereis function
> Is now a decent bit faster
> Has option for ignoring system files
> Has option to scan all drives, as opposed to just one
> Now all options can be passed as sys arguments, folowing format: `GPT whereis FILENAME DRIVE IGNORESYSFILES(y/n)`

-----

# v1.5 Patchnotes:

### Added ActivateWindows function
> Activates Windows using default keys
### Made Help function more clear
> Describes how to call diffrent functions from cmd

-----

# v1.6 Patchnotes:

### Added a prompt for restarting in ActivateWindows function
### Fixed Minor mistakes

-----

# v1.7 Patchnotes:

### Now checks if the program is on the latest release
> Checks the latest tag on github
> If you're not on the latest version, it will give you a link to download the latest release

-----

# v1.8 Patchnotes:

### Fixed ActivateWindows function
> The restart function actually works now
> It's now more clear that you have to press enter after an error message is given after trying to check the latest version
> Added a check for if you already have a Windows key
### Fixed a bunch of small bugs and comment errors

-----

# v1.9 Patchnotes:

### Added speed tester for drives *(WIP)*
> Can be ran on any drives recognized by Windows
> Can check all drives or specified drive
> (Read speed is currently broken)
### Added port scanner
> Can scan any range of ports
> `*` will scan all ports
> `/` will scan the 75 most common ports

-----

# v1.10 Patchnotes:

### Fixed speedtest
> Added an `s` to the time taken for writing (it was already present on read speeds)
> Fixed speeds to actually be correct (i think?)
### Made timeout for port scanner dynamic
### Added a function to output a formated view of a directory and it's subdirectories
> Has an option to show and hide files
> Has an option to show and hide hidden files
> Outputs to a file called `FolderStructure.txt`
> Directory of said file can be changed or if left empty will default to the current users desktop
### Updated `readme.md` to be more clear on how to use GPT
### Changed `setup.bat`
> The name of the `.exe` will now always be `GPT`
> All modules are now automatically installed
### Fixed a bug where GPT would close itself after running a tool rather than going back to the main menu
### Rewrote the patchnotes and made them a `.md` file


