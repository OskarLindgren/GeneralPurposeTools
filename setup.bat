@echo off
color 0e
CHCP 65001
echo ^◄ Made by Oskar Lindgren (https://github.com/OskarLindgren) ^►
echo.
set /p a="Enter the exe name: "
if [%a%]==[] ( 
    echo.
    echo Please enter a name
    pause
    EXIT /B 1
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    pyinstaller --noconfirm --onefile --console --icon "NONE" --name %a% --add-data "./functions;functions/" --add-data "./main.ini;."  "./main.py"
    rmdir /s /q build
    del /f / s /q %a%.spec
    ren dist output
    echo.
    echo generated exe as %a%.exe in the output folder
    echo.
    pause
    EXIT /B 1
)