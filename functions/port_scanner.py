import socket
import re
import os
import ping3
import time
import threading
import psutil
import queue
from contextlib import closing

def portScanner(ip: str=None, ports:str=None) -> None:
    os.system("Title GPT - Port Scanner")

    ### statics
    ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_min = int(0)
    port_max = int(65535)
    ptp = []

    ### OPTIONS

    # fix ip
    if ip == None:
        ip = input("Please enter a valid ip adress: ")

    while True:
        if ip_pattern.search(ip):
            break
        ip = input("Please enter a valid ip adress: ")

    # fix ports
    if ports == None:
        ports = str(input("Please enter a valid port/port range: "))
    
    if "*" in ports:
        portA, portB = port_min, port_max
    elif "/" in ports:
        ptp = [13, 19, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 111, 113, 123, 135, 137, 139, 143, 161, 389, 443,
               445, 500, 587, 993, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1050, 1723, 1863, 3389, 3783, 4444,
               4567, 4664, 5000, 5060, 5353, 5678, 7159, 7547, 7676, 8000, 8080, 8081, 8082, 8594, 8888, 9300, 
               9301, 9302, 9400, 9987, 10000, 12203, 13777, 18067, 20102, 23000, 27003, 27374, 27910, 27960, 28960,
               29900, 30005, 34297, 51111, 64738]
    else:
        done = False
        port_splitstrs = [',', '-', ':', ' '] # any extra spaces don't matter, as they are stripped during type conversion
        while True:
            if ports == None or ports == "":
                ports = str(input("Please enter a valid port/port range: "))
            # try making it a single int (will fail if not (0 < int.count < 2))
            try:
                ports = int(ports)
                if ports < port_min or ports > port_max:
                    print("port out of range")
                    input("...")
                    return
                break # break out of loop if type conversion was succesfull
            except (ValueError, TypeError):
                # turn it into 2 ints of it fails
                for splitstr in port_splitstrs:
                    if type(ports) == str:
                        if splitstr in ports:
                            ports = ports.split(splitstr)
                            if len(ports) > 2:
                                print("Too many ports in range")
                                input("...")
                                return
                            portA, portB = map(int, ports)
                            portB += 1
                            # make sure that the ports are in the correct range
                            if portA < port_min or portB > port_max:
                                print("1 or more ports were out of range")
                                input("...")
                                return
                            elif portA >= portB-1:
                                print("ports must be in a positive range")
                                input("...")
                                return
                            done = True # break out of the above for loop
                    # if the for loop finishes without breaks, run the next iteration
                    else:
                        continue
                    # if the for loop was broken out of, break out of the while loop
                    if done:
                        break # break out of for loop
            if done:
                break # break out of while loop


    ### CHECKS   

    # make sure the ip is accesible
    print("Checking IP (please wait up to a second)")
    try:
        ping = ping3.ping(ip, timeout=1)
        if type(ping) != float:
            print("The ip is down or is not responding to pings (or is just too damn slow)")
            input("...")
            return
    except Exception:
        print("General IP failure")
        input("...")
        return

    print(f"{ip} responded in ~{round(ping*1000, 1)} ms\n┌──────────")

    ### START CHECKING PORTS

    ## check singular port
    if type(ports) == int:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            if sock.connect_ex((ip, ports)) == 0:
                print(f"├ port {ports} is open")
            else:
                print(f"│ port {ports} is closed")
        print("└──────────" + "\n--Done--")
        input("...")
        return

    ## check multiple ports
    if ptp == []:
        ptp = list(range(portA, portB))
    q = queue.Queue()
    q.put(int(-1))

    class pinger(threading.Thread):
        def __init__(self, threadID):
            threading.Thread.__init__(self)
            self.threadID = threadID

        def run(self):
            while True:
                try:
                    checkPort(ip)
                except IndexError:
                    break

    def checkPort(ip):
        i = int(q.get())
        i+=1
        q.put(i)
        port = ptp[i]

        print(f"| {port}", end="\r")
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            startTime = time.time()
            if sock.connect_ex((ip, port)) == 0:
                ping = time.time() - startTime
                # create a short delay so that port checking stays in sync and ports don't jumble
                time.sleep(1-ping)
                print(f"├ port {port} is open")
            else:
                if len(ptp) <= 21: # if the user is scanning <= 20 (it says 21 but computer count from 0 you count from 1 bla bla bla) ports, show the ports that are closed aswell
                    print(f"│ port {port} is closed")

    # create pingers
    pingers = []
    for n in range(psutil.cpu_count(True)):
        pingers.append(pinger(n))
    # starting pingers
    for cur_pinger in pingers:
        # create a short delay so that ports are spread out evenly over a second.
        time.sleep(round(1/psutil.cpu_count(True)*n, 3))
        cur_pinger.start()
    # stopping pingers
    for cur_pinger in pingers:
        cur_pinger.join()
        

    print("└──────────" + "\n--Done--")
    input("...")
    return

if __name__ == '__main__':
    portScanner(ip=None, ports=None) # alex: 172.67.192.218