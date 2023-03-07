import os
import win32api
import time

def Test_speed(drive=None):
    os.system("title " + "GPT - Speed Test")
    size = 128 # MB

    ### OPTIONS

    # checks if a drive was passed when calling 
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
                drive = input("What drive do you want to test? (C | D | E | * | etc)\n").title()
                if drive.title() + ":\\" in win32api.GetLogicalDriveStrings().split('\000')[:-1] or '*' in drive:
                    break
                else:
                    os.system("cls")
                    print("Can't find drive: ", drive)
    # if not, it asks
    else:
        while True:
            drive = input("What drive do you want to test? (C | D | E | * | etc)\n").title()
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

    os.system('cls')
    print("It is worth noting that times may be a bit off, especially read speeds. But it gives you a rough idea")
    for drive in drives:
        # bruh
        if ":\\" not in drive:
            drive += ":\\"

        # if the drive is "c", it wont allow you to place a file in root
        if "C" in drive.title():
            location = f"{drive.title()}Temp\\temp_speed_test.txt"
        else:
            location = f"{drive.title()}temp_speed_test.txt"

        # Write
        print("\nTesting", drive.title(), "\n")
        start_time = time.time()
        with open(location, "w") as write:
            try:
                write.write("0" * 1024 * 1024 * size) # We want size in MB
                write.close()
                finish_time = time.time()

            except Exception as e:
                # try removing the file if it was created
                try: write.close(), os.remove(location)
                except OSError: pass

                print("Something went wrong...\n" + str(e))
                input()
                return
        time_taken = round(finish_time-start_time, 1)
        print(f"Wrote {size}MB in {time_taken}s ({round(size/time_taken, 2)}MB/s)")

        # reset times
        start_time, finish_time = None, None

        # clear file variable/cache
        del(write)

        # Read

        start_time = time.time()
        with open (location, "r") as read:
            try:
                data = read.read()
                # performe some computations with the data to make sure that python is reading it properly
                length = len(data)
                data = str(length) # this in and of itself takes <1ms on most modern systems.
                read.close()
                finish_time = time.time()

            except Exception as e:
                # try removing the file
                try: read.close(), os.remove(location)
                except OSError: pass

                print(f"Something went wrong...\n{e}")
                input()
                return
        time_taken = finish_time-start_time
        print(f"Read {int(size)}MB in {round(time_taken, 1)}s ({round(size/time_taken, 2)}MB/s)")

        # Clean up
        try: os.remove(location)
        except OSError: pass

    return


if __name__ == '__main__':
    Test_speed()