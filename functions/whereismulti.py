import win32api
import os
import queue
import threading
import psutil

def WhereIs(lookup_name=None, drive=None, ignore_system_files=None):
    os.system("title " + "GPT - WhereIs")
    banned_dirs = ["$recycle.bin", "$win", "windows"]

    ### OPTIONS

    # checks if a filename was passed when calling WhereIs()
    if lookup_name != None:
        pass
    else:
        # if not, it asks
        lookup_name = input("What file do you want to look up?\n")


    # checks if a drive was passed when calling WhereIs()
    if drive != None:
        # checks if it actually is a drive
        if drive.title() + ":\\" in win32api.GetLogicalDriveStrings().split('\000')[:-1] or '*' in drive:
            # if * was not written (a drive was selected) only add that drive to the list of drives to search
            if '*' not in drive:
                drives = [drive]
            # otherwise add all drives
            else:
                drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
        # if it's not a drive, ask the user for a drive
        else:
            print("It seems you passed something that's not a drive")
            while True:
                drive = input("What drive do you want to search? (C | D | E | * | etc)\n").title()
                if drive.title() + ":\\" in win32api.GetLogicalDriveStrings().split('\000')[:-1] or '*' in drive:
                    break
                else:
                    os.system("cls")
                    print("Can't find drive: ", drive)
    # if not, it asks
    else:
        while True:
            drive = input("What drive do you want to search? (C | D | E | * | etc)\n").title()
            if drive.title() + ":\\" in win32api.GetLogicalDriveStrings().split('\000')[:-1] or '*' in drive:
                break
            else:
                os.system("cls")
                print("Can't find drive: ", drive)
        # if * was not written (a drive was selected) only add that drive to the list of drives to search
        if '*' not in drive:
            drives = drive
        # otherwise add all drives
        else:
            drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]


    # checks if ignore_system_files was passed when calling WhereIs()
    if ignore_system_files != None:
        if ignore_system_files.lower() == "y":
            ignore_system_files = True
        elif ignore_system_files.lower() == "n":
            ignore_system_files = False
        else: # an incorrect option was passed, so we ask
            if input("Ignore system files? Y/n: ").lower() == "n":
                ignore_system_files = False
            else:
                ignore_system_files = True
    # otherwise, ask
    else:
        if input("Ignore system files? Y/n: ").lower() == "n":
            ignore_system_files = False
        else:
            ignore_system_files = True
    

    ### ACTUALLY SEARCH

    ## set up threads

    q = queue.Queue()
    q.put(None)

    class searcher(threading.Thread):
        def __init__(self, threadID):
            threading.Thread.__init__(self)
            self.threadID = threadID

        def run():
            location = str(q.get())
            


    threads = psutil.cpu_count(True)

    # do this for all selected drives
    for drive in drives:
        drive=drive[0]
        try:
            os.chdir(drive+":\\")
        except Exception:
            # this should never be called unless there is data manipulation
            print("You didn't input a drive correctly!")
            input("Enter to return...")
            return

        print(f"Searching... {drive.title()}:\\", end="\r")

        # get's current dir
        for cur_dir, dirs, files in os.walk(os.getcwd()):
            # "snips" system directories if the user wants to ignore system files
            if ignore_system_files:
                for directory in dirs:
                    for banned_dir in banned_dirs:
                        if banned_dir in directory.lower():
                            dirs.remove(directory)
            # for every file in the dir
            for file in files:
                # make a proper path, if it's the root folder (c:, d:, etc), don't add another \
                if len(cur_dir) != 3:
                    path = cur_dir + "\\" + file
                else:
                    path = cur_dir + file
                # if the file has the lookup_name (we use file opposed to path because path would return positive if the folder fits the check for lookup_name)
                if lookup_name in file:
                    # if path is a file
                    if lookup_name in file and os.path.isfile(path):
                        print("Found file at: " + path)
                    print("Working...", end="\r")


    print("Press enter to continue...")
    input()
    return

if __name__ == '__main__':
    WhereIs()