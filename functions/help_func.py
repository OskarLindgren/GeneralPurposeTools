import os

def Help(github=None, authors=None):
    os.system("title " + "GPT - Help")
    print(f"Commands")
    print(f"help, h - Displays commands and options")
    print(f"version, v - Displays program version")
    print(f"sinfo - Displays system information")
    print(f"whereis FILENAME DRIVE IGNORESYSFILES( y | n ) - Finds path(s) to file searched for")
    print(f"calculator, calc - Opens a simple calculator")
    print(f"activate_windows, ActWin - Activates windows using black magic")
    print(f"speed_test, test_speed, speed DRIVE SIZE(MB)- Tests the speed of a drive")
    print(f"port_scanner, scan_port, pscan IP PORT( single | range | * | / ) - Scan open ports on a given ip adress")

    print("\nrun commands by selecting them or typing GPT <COMMAND> in cmd")
    if github == None:
        print("\nGithub & Authors not found")
    else:
        print(f"\n{github}\nMade by: {' & '.join(authors)}")
    
    print("Press enter to continue...")
    input()
    return

if __name__ == '__main__':
    Help()