import os, sys, time
from datetime import date

#Value
today = date.today()

#month day year
now = today.strftime("%B %d, %Y")

os.system("clear")
os.system("figlet KNIFE")
print("welcome to this beta\n")
print("Now: ", now)


#Functions
def num1():
    os.system("clear")
    os.system("figlet Check IP\n")
    os.system("sudo netdiscover")

def num2():
    os.system("clear")
    os.system("figlet SCAN...")
    print("use you brain!\n")
    sc = input("IP/URL: ")
    os.system("clear")
    print("Waiting...")
    time.sleep(5)
    os.system("nmap -v -A " + sc)
    print("\n")
    check = input("Scan Complete...Do you want to return? Y/N> ")
    if check == "Y" or check == "y":
        print("OK LET'S GO!")
        time.sleep(2)
        os.system("python3 knife.py")
    elif check == "N" or check == "n":
        print("Good Bye :) ")
        time.sleep(2)
        os.system("clear")
        sys.exit()

def num3():
    os.system("clear")
    os.system("figlet UPDATE!")
    print("No have a update :) ")
    time.sleep(3)
    os.system("python3 knife.py")



#MENU
print("\n[1] Check IP")
print("[2] Scan IP or Website")
print("[3] Update KNIFE")
print("[00] Exit\n")
kni = input("sel> ")

if kni == "1" or kni == "01":
    num1()

elif kni == "2" or kni == "02":
    num2()

elif kni == "3" or kni == "03":
    num3()

elif kni == "0" or kni == "00":
    print("Waiting for Exit")
    time.sleep(3)
    os.system("clear")
    sys.exit()