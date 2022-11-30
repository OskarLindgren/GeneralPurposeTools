import os
import platform
import psutil
import GPUtil
import win32api
import urllib.request
import socket
import netifaces

def Sinfo():
    os.system("title " + "CatTools - System Info")
    print("Please wait... Gathering system information.")
    os.system("cls")
        
    # OS
    if platform.machine()  == "AMD64":
        arch = "x64 or AMD64"
    else:
        arch = platform.machine()
        
    print(f"=========================\n\nOPERATING SYSTEM\n\nArchitecture: {arch}\nVersion: {platform.version()}\nPlatform: {platform.platform()}")
        
    # CPU
    print(f"=========================\n\nCPU\n\nName: {platform.processor()}\nCores: {psutil.cpu_count(False)}\nThreads: {psutil.cpu_count(True)}\nUsage: {psutil.cpu_percent()}%")
        
    # RAM
    print(f"=========================\n\nMEMORY\n\nTotal Physical Memory: {round(psutil.virtual_memory().total/1024/1024/1024, 2)}GB\nUsage: {psutil.virtual_memory()[2]}%")
       
    # GPU
    GPUs = GPUtil.getGPUs()
    if len(GPUs) == 1:
        gpu = GPUs[0]
        print(f"=========================\n\nGPU\n\nLoad: {round(gpu.load*100, 2)}%\nMemLoad: {round(gpu.memoryUtil*100, 2)}%\n")
    else:
        for gpu in GPUs:
            print(f"=========================\n\nGPU{gpu.id}\n\nLoad: {round(gpu.load*100, 2)}%\nMemLoad: {round(gpu.memoryUtil*100, 2)}%")
    
    
    # Drives
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    print(f"=========================\n\nDISK\n")
    for drive in drives:
        letter = drive
        drive = f"Total: {round(psutil.disk_usage(drive).total/1024/1024/1024)}GB Used: {round(psutil.disk_usage(drive).used/1024/1024/1024)}GB Free: {round(psutil.disk_usage(drive).free/1024/1024/1024)}GB"
        print(f"{letter} | {drive}")
        
    # Network
    print(f"=========================\n\nNETWORK\n\nExternal IPv4: {urllib.request.urlopen('https://ident.me').read().decode('utf8')}\nInternal IPv4: {socket.gethostbyname(socket.gethostname())}\nDefault Gateway: {netifaces.gateways()['default'][netifaces.AF_INET][0]}")

    print("Press enter to continue...")
    input()
    return

if __name__ == '__main__':
    Sinfo()