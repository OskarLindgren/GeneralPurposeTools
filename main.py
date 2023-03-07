import os
import sys
import configparser

from functions import whereis
from functions import sinfo
from functions import calculator
from functions import help_func
from functions import version
from functions import activate_windows
from functions import check_latest_version
from functions import speed_test
from functions import port_scanner
from functions import display_dir

# Locating main.ini
config = configparser.ConfigParser()
config_file = f'{os.path.dirname(os.path.abspath(__file__))}\main.ini'
config.read(config_file)

MAIN = config['MAIN']

version_number = config.get('MAIN', 'version_number')
github = config.get('MAIN', 'github')
authors = config.get('MAIN', 'authors').split(", ")


os.system("title " + "General Purpose Tools") # sets title of cmd window

for arg in sys.argv: # le bruh
    arg = arg.lower()

options = """
0) Exit
1) Help
2) Version
3) Calculator
4) Sinfo
5) WhereIs
6) Activate Windows
7) Speed Test
8) Port Scanner
9) Show Folder Hierarchy
"""  

# main runtime     
def Start():
    check_latest_version.CheckVersion(version=version_number)

    os.system("cls")
    if len(sys.argv) < 2: # the actual file counts as an argv, thus this means if 1 or more parameters were passed
        os.system("title " + "General Purpose Tools")
        print("Select a tool:")
        print(options)
        
        try:
            selection = int(input())
        except ValueError:
            Start()
        except KeyboardInterrupt:
            sys.exit(0)
        
        
        if selection == 0:
            os.system("cls")
            sys.exit(0)
        elif selection == 1:
            os.system("cls")
            help_func.Help(github, authors)
            Start()
        elif selection == 2:
            os.system("cls")
            version.Version(version_number)
            Start()
        elif selection == 3:
            os.system("cls")
            calculator.Calculator()
            Start()
        elif selection == 4:
            os.system("cls")
            sinfo.Sinfo()
            Start()
        elif selection == 5:
            os.system("cls")
            whereis.WhereIs()
            Start()
        elif selection == 6:
            os.system("cls")
            activate_windows.Activate_windows()
        elif selection == 7:
            os.system("cls")
            speed_test.Test_speed()
        elif selection == 8:
            os.system("cls")
            port_scanner.portScanner()
        elif selection == 9:
            os.system("cls")
            display_dir.displayDir()
        else:
            print("BRUH")
            try:
                input()
            except KeyboardInterrupt:
                sys.exit(0)
            Start()

    elif any(sys.argv[1] == s for s in ["help", "h"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        help_func.Help(github, authors) 
        Start() 
    elif any(sys.argv[1] == s for s in ["version", "v"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        version.Version(version_number)
        Start()
    elif any(sys.argv[1] == s for s in ["sinfo"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        sinfo.Sinfo()
        Start()
    elif any(sys.argv[1] == s for s in ["calc", "calculator"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        calculator.Calculator()
        Start()
    elif any(sys.argv[1] == s for s in ["whereis"]):
        # depending on how many args are passed, call it correctly
        os.system("cls")
        if len(sys.argv) == 5:
            whereis.WhereIs(sys.argv[2], sys.argv[3], sys.argv[4])
        elif len(sys.argv) == 4:
            whereis.WhereIs(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            whereis.WhereIs(sys.argv[2])
        else:
            whereis.WhereIs()
        sys.argv = [] # clear sys.argv
        Start()
    elif any(sys.argv[1] == s for s in ["activatewindows", "actwin"]):
        os.system("cls")
        activate_windows.Activate_windows()
    elif any(sys.argv[1] == s for s in ["speed_test", "test_speed", "speed"]):
        os.system("cls")
        if len(sys.argv) == 3:
            speed_test.Test_speed(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 2:
            speed_test.Test_speed(sys.argv[2])
        else:
            speed_test.Test_speed()
        sys.argv = [] # clear sys.argv
    elif any(sys.argv[1] == s for s in ["port_scanner", "scan_port", "pscan"]):
        os.system("cls")
        if len(sys.argv) == 4:
            port_scanner.portScanner(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            port_scanner.portScanner(sys.argv[2])
        else:
            port_scanner.portScanner()
        sys.argv = [] # clear sys.argv
    elif any(sys.argv[1] == s for s in ["display_dir", "print_dir", "ddir", "pdir"]):
        os.system("cls")
        if len(sys.argv) == 5:
            display_dir.displayDir(sys.argv[2], sys.argv[3], sys.argv[4])
        elif len(sys.argv) == 4:
            display_dir.displayDir(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            display_dir.displayDir(sys.argv[2])
        else:
            display_dir.displayDir()
        sys.argv = [] # clear sys.argv

    Start()
        

# run
if __name__ == '__main__':
    Start()