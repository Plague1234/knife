import os, sys, time
from datetime import datetime, date


################################
# Stroage Functions and more...#
################################

def comming_soon():
    os.system("clear")
    print("""
                             d8b                          
                         88P              d8P         
                        d88            d888888P       
?88   d8P?88,.d88b, d888888   d888b8b    ?88'   d8888b
d88   88 `?88'  ?88d8P' ?88  d8P' ?88    88P   d8b_,dP
?8(  d88   88b  d8P88b  ,88b 88b  ,88b   88b   88b    
`?88P'?8b  888888P'`?88P'`88b`?88P'`88b  `?8b  `?888P'
           88P'                                       
          d88                                         
          ?8P                                         

    """)

#Value
today = datetime.today()

#month day year
now = today.strftime("%B %d %Y, %H:%M:%S " + " Have a nice day :)")

#Date Now
print(time.strftime("%Y-%m-%d"))

def start():
    datetz = '2021-09-8'
    expirez = time.strftime("%Y-%m-%d")
    if expirez >= datetz:
        os.system("clear")
        print("Script Expired! Please Update")
        time.sleep(5)

def check_status():
#Status Check
    dateted = '2021-09-8'
    expireDate = time.strftime("%Y-%m-%d")
    if expireDate >= dateted:
        print("Status: Expired")
    else:
        print("Status: Running")

#Functions
def num1():
    os.system("clear")
    comming_soon()
    time.sleep(5)
    print("Coming Soon...")
    time.sleep(2)
    check = input("Do you want to return to script? Y/N> ")
    if check == "Y" or check == "y":
        print("OK LET'S GO!")
        time.sleep(2)
        os.system("python3 knife.py")
    elif check == "N" or check == "n":
        print("Good Bye :) ")
        time.sleep(2)
        os.system("clear")
        sys.exit()
    else:
        print("\n ERROR WRONG INPUT")
        time.sleep(3)
        sys.exit()

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
    check = input("Scan Complete...Do you want to return to script? Y/N> ")
    if check == "Y" or check == "y":
        print("OK LET'S GO!")
        time.sleep(2)
        os.system("python3 knife.py")
    elif check == "N" or check == "n":
        print("Good Bye :) ")
        time.sleep(2)
        os.system("clear")
        sys.exit()
    else:
        print("\n ERROR WRONG INPUT")
        time.sleep(3)
        sys.exit()

def num3():
    os.system("clear")
    os.system("figlet Scan port and IP!")
    print("\nexample: IP: 127.0.0.1 PORT:80\nTake a long time...")
    ip = input("IP: ")
    port = input("PORT: ")
    ip2 = input("IP2: ")
    port2 = input("PORT2: ")
    time.sleep(4)
    os.system("nmap -v -sn " + ip+ "/"+port + " " + ip2+ "/"+port2)
    time.sleep(3)
    check = input("Scan Complete...Do you want to return to script? Y/N> ")
    if check == "Y" or check == "y":
        print("OK LET'S GO!")
        time.sleep(2)
        os.system("python3 knife.py")
    elif check == "N" or check == "n":
        print("Good Bye :) ")
        time.sleep(2)
        os.system("clear")
        sys.exit()
    else:
        print("\n ERROR WRONG INPUT")
        time.sleep(3)
        sys.exit()

def update():
    os.system("clear")
    os.system("figlet UPDATE!")
    os.system("rm -rf KNIFE")
    os.system("git clone https://github.com/Plague1234/KNIFE")
    os.system('mv KNIFE/knife/knife.py $HOME/KNIFE/knife/')
    time.sleep(5)
    os.system("rm -rf KNIFE")
    print("Update Complete...")
    time.sleep(3)
    os.system("python3 knife.py")

##################
#EXPIRED FUNCTION#
##################
def expired():
#Expired Day
    datet = '2021-09-8'

    ExpirationDate = time.strftime("%Y-%m-%d")
    if ExpirationDate >= datet:
        os.system("clear")
        print("Wait...I'm looking for the new version")
        time.sleep(10)
        print("Script Expired Update now...")
        time.sleep(3)
        os.system("clear")
        print("Don't forget to update :)")
        sys.exit()
        os.system("python3 knife.py")
    elif ExpirationDate == datet:
        os.system("clear")
        print("Last Day Please Update")
        time.sleep(2)
    else:
        os.system("clear")
        time.sleep(2)
        print("OK...Not have a update...")
        time.sleep(3)
        