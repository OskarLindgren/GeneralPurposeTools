import os
import sys
import ctypes
import time
import subprocess
from platform import win32_edition as edition
from platform import release
from threading import Thread

stop_flag = True

def kill_popup():
    global stop_flag
    while stop_flag:
        time.sleep(.25)
        try: 
            os.system("taskkill /f /im wscript.exe >nul 2>&1")
        except:
            print("Couldn't kill popup")
            pass

def Activate_windows():
    os.system("title GPT - Activate Windows")

    # Make sure the program is in admin mode
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    # Check if windows is already activated
    try:
        wkey = subprocess.check_output(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", creationflags=0x08000000).decode().rstrip()
        print("You already have windows activated!")
        print("Press enter to exit...")
        input()
        return
    except Exception: # this means there is no windowskey
        pass

    global stop_flag
    Thread(target=kill_popup).start()

    print(f"Windows {release()} {edition()} Edition detected!")
    print("\nInstalling product key...")

    keys = {
        "10": {
            "Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
            "Home N": "3KHY7-WNT83-DGQKR-F7HPR-844BM",
            "Home Single Language": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
            "Home Country Specific": "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
            "Professional": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
            "Professional N": "MH37W-N47XK-V7XM9-C7227-GCQG9",
            "Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
            "Education N": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
            "Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
            "Enterprise N": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
        },
        "8": {
            "Core": "BN3D2-R7TKB-3YPBD-8DRP2-27GG4",
            "Core Single Language": "2WN2H-YGCQR-KFX6K-CD6TF-84YXQ",
            "Professional": "NG4HW-VH26C-733KW-K6F98-J8CK4",
            "Professional N": "XCVCF-2NXM9-723PB-MHCB7-2RYQQ",
            "Professional WMC": "GNBB8-YVD74-QJHX6-27H4K-8QHDG",
            "Enterprise": "32JNW-9KQ84-P47T8-D8GGY-CWCK7",
            "Enterprise N": "JMNMF-RHW7P-DMY6X-RF3DR-X2BQT"
        },
        "8.1": {
            "Core": "M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK",
            "Core N": "7B9N3-D94CG-YTVHR-QBPX3-RJP64",
            "Core Single Language": "BB6NG-PQ82V-VRDPW-8XVD2-V8P66",
            "Professional": "GCRJD-8NW9H-F2CDX-CCM8D-9D6T9",
            "Professional N": "HMCNV-VVBFX-7HMBH-CTY9B-B4FXY",
            "Professional WMC": "789NJ-TQK6T-6XTH8-J39CJ-J8D3P",
            "Enterprise": "MHF9N-XY6XB-WVXMC-BTDCT-MKKG7",
            "Enterprise N": "TT4HM-HN7YT-62K67-RGRQJ-JFFXW"
        },
        "7": {
            "Starter": "SK8WH-JVQDM-C9HVC-YR2XC-8M76G",
            "Home Basic": "V6V3G-9DB2T-BD4VC-44JVQ-6BVR2",
            "Home Premium": "TWF78-W7H8T-KXD8C-YDFCQ-HK4WG",
            "Professional": "7YWX9-W3C2V-D46GW-P722P-9CP4D",
            "Ultimate": "JHY4Q-NH85H-XK8VD-9Y68P-RFQ43",
            "Enterprise": "33PXH-7Y6KF-2VJC9-XBBR8-HVTHH",
            "Enterprise E": "C29WB-22CC8-VJ326-GHFJW-H9DH4"
        },
        "Vista": {
            "Starter": "X9PYV-YBQRV-9BXWV-TQDMK-QDWK4",
            "Home Basic": "RCG7P-TX42D-HM8FM-TCFCW-3V4VD",
            "Home Premium": "X9HTF-MKJQQ-XK376-TJ7T4-76PKF",
            "Business": "4D2XH-PRBMM-8Q22B-K8BM3-MRW4W",
            "Ultimate": "VMCB9-FDRV6-6CDQM-RV23K-RP8F7"
        }
    }

    key = keys[release()][edition()]

    os.system(f"slmgr /ipk {key}")
    print(f'Product key "{key}" successfully installed!')
    print("\nChanging the KMS server...")
    os.system("slmgr /skms kms10.msguides.com")
    print("KMS server successfully set to: kms10.msguides.com")
    print("\nActivating system...")
    os.system("slmgr /ato")
    print(f"Windows {release()} {edition()} Edition was activated!\n")
    stop_flag = False # stops killing popups

    if input("Do you want to restart your pc now? Y/n\n").lower() == "n":
        print("Press enter to exit...")
        input()
        return
    else:
        for seconds in range(5):
            print(f"Restarting in {5-seconds} seconds!", end="\r")
            time.sleep(1)
        os.system("shutdown /r /t 1")


if __name__ == '__main__':
    Activate_windows()