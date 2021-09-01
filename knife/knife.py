import os, sys, time
from datetime import datetime, date
import readline
from core.kncore import *

def main():
    os.system("clear")
    os.system("figlet KNIFE")
    print("Creator: Painkiller")
    print("Team: Remaster")
    print("Version 1.2.0\n")
    print("Now: ", now)
    check_status()

    print("\n[01] Check IP")
    print("[02] Scan IP or Website")
    print("[03] Scan IP with port")
    print("[UPDATE] For PC Linux MacOS")
    print("[00] Exit\n")
    kni = input("sel> ")

    if kni == "1" or kni == "01":
        expired()
        num1()

    elif kni == "2" or kni == "02":
        expired()
        num2()

    elif kni == "3" or kni == "03":
        expired()
        num3()

    elif kni == "update" or kni == "UPDATE":
        update()

    elif kni == "0" or kni == "00":
        print("Waiting for Exit")
        time.sleep(3)
        os.system("clear")
        sys.exit()

    else:
        print("\n ERROR WRONG INPUT")
        time.sleep(3)
        os.system("python3 knife.py")
start() #IF EXPIRED
main()