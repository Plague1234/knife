import os, sys, time
from datetime import datetime, date
from time import sleep as timeout
from core.kncore import *

def main():
    banner()
    print("Description : You can scan ip or url :)\n\n\n")
    print("Version 1.2.5\n")
    print("RedEyez-Sec")
    print("Contact us : redeyezsec@gmail.com")
    print("Now: ", now)
    check_status()

    print("\n[01] What's my ip address?")
    print("[02] Scan with script for vul-network")
    print("[03] Ping Scan")
    print("[04] Scan for Open Ports")
    print("[05] Scan Hosts")
    print("[06] Identify Operating Systems")
    print("[07] Stealth Scanning")
    print("[UPDATE] For PC Linux MacOS")
    print("[00] Exit\n")
    kni = input("sel > ")

    #1 Check IP ADDR
    if kni == "1" or kni == "01":
        num1()

    #2 Scan for vul
    elif kni.strip() == "2" or kni.strip() == "02":
        os.system('clear')
        os.system("figlet Vulscript")
        print("[01] Vulscan")
        print("[02] Vulners")
        print("[03] DOS ATTACK Vulner scan")
        print("\n [00] Back to main menu\n")
        vul = input("sel > ")
        for vulx in vul.split():
            if vul.strip() == "01" or vul.strip() == "1": vulscan()
            elif vul.strip() == "02" or vul.strip() == "2": vulners()
            elif vul.strip() == "03" or vul.strip() == "3": dos()
            elif vul.strip() == "00" or vul.strip() == "0": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1)

    #3 Ping Scan
    elif kni == "3" or kni == "03":
        num3()

    #4 Open Ports
    elif kni.strip() == "4" or kni.strip() == "04":
        os.system('clear')
        os.system('figlet Open Ports')
        print("\n[01] Parameter Scan")
        print("[02] Particular Scan")
        print("[03] Range Scan")
        print("[04] Tport Scan")
        print("\n [00] Back to main menu\n")
        p = input("sel > ")
        for px in p.split():
            if p.strip() == "01" or p.strip() == "1": parameter()
            elif p.strip() == "02" or p.strip() == "2": particular()
            elif p.strip() == "03" or p.strip() == "3": range()
            elif p.strip() == "04" or p.strip() == "4": tport()
            elif p.strip() == "00" or p.strip() == "0": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1)

    #5 Hosts
    elif kni.strip() == "5" or kni.strip() == "05":
        os.system('clear')
        os.system('figlet Hosts')
        print("\n[01] Multihosts Scan")
        print("[02] Subnets Scan")
        print("[03] Fullrange Scan")
        print("\n [00] Back to main menu\n")
        hx = input("sel > ")
        for hxx in hx.split():
            if hx.strip() == "01" or hx.strip() == "1": multihosts()
            elif hx.strip() == "02" or hx.strip() == "2": subnets()
            elif hx.strip() == "03" or hx.strip() == "3": fullrange()
            elif hx.strip() == "00" or hx.strip() == "0": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1)

    #6 Identify OS
    elif kni == "6" or kni == "06":
        osa()

    #7 Stealth Scanning
    elif kni.strip() == "7" or kni.strip() == "07":
        os.system('clear')
        os.system('figlet Sscanning')
        print("\n[01] Stealth Scan")
        print("[02] Scans serveral(nost commonly used)")
        print("\n[00] Back to main menu\n")
        ssc = input("sel > ")
        for sscx in ssc.split():
            if ssc.strip() == "01" or ssc.strip() == "1": stealth()
            elif ssc.strip() == "02" or ssc.strip() == "2": serveral()
            elif ssc.strip() == "00" or ssc.strip() == "0": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1)

    elif kni == "update" or kni == "UPDATE":
        update()

    elif kni.strip() == "0" or kni.strip() == "00":
        sys.exit()

    else:
        print("\n ERROR WRONG INPUT")
        time.sleep(3)
        restart_program()

if __name__ == "__main__":
    os.system("clear")
    main()
start() #IF expired