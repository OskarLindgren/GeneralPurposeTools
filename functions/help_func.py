import os

def Help(github=None, authors=None):
    os.system("title " + "General Purpose Tools - Help")
    print(f"Commands")
    print(f"help, h - Displays commands and options")
    print(f"version, v - Displays program version")
    print(f"sinfo - Displays system information")
    print(f"whereis FILENAME DRIVE IGNORESYSFILES(y/n) - Finds path(s) to the file searched for")
    print(f"calculator, calc - Opens a simple calculator")
    if github == None or authors == None:
        print("\nGithub & Authors not found")
    else:
        print(f"\n{github}\nMade by: {' & '.join(authors)}")
    
    print("Press enter to continue...")
    input()
    return

if __name__ == '__main__':
    Help()
