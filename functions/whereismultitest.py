import win32api
import os
import queue
import threading
import psutil

def WhereIs(lookup_name=None, drive=None, ignore_system_files=None):
    banned_dirs = ["$recycle.bin", "$win", "windows"]
    

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
    drives = [drive]

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
    WhereIs(lookup_name=input("Lookup name: "), drive="C")