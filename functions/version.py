import os

def Version(version_number=None):
    os.system("title " + "CatTools - Version")
    if version_number == None:
        print("Version not found")
    else:
        print(f"Version: {version_number}\n")
    
    print("Press enter to continue...")
    input()
    return

if __name__ == '__main__':
    Version()