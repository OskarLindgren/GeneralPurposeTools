@echo off
color 0e
CHCP 65001
echo ^◄ Made by Oskar Lindgren (https://github.com/OskarLindgren) ^►
echo installing modules
pip install -r requierments.txt
echo.
pyinstaller --noconfirm --onefile --console --icon "NONE" --name "GPT" --add-data "./functions;functions/" --add-data "./main.ini;." "./main.py"
rmdir /s /q build
del /f / s /q GPT.spec
ren dist output
echo.
echo generated exe as GPT.exe in the output folder
echo.
pause
EXIT /B 1
