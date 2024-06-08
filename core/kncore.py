import os, sys, time
from datetime import datetime, date
import urllib.request
from subprocess import check_output as inputstream


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

def banner():
    print("""
        ██ ▄█▀ ███▄    █  ██▓  █████▒▓█████
        ██▄█▒  ██ ▀█   █ ▓██▒▓██   ▒ ▓█   ▀
        ▓███▄░ ▓██  ▀█ ██▒▒██▒▒████ ░ ▒███
        ▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█▒  ░ ▒▓█  ▄
        ▒██▒ █▄▒██░   ▓██░░██░░▒█░    ░▒████▒
        ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ▒ ░    ░░ ▒░ ░
        ░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░ ░       ░ ░  ░
        ░ ░░ ░    ░   ░ ░  ▒ ░ ░ ░       ░
        ░  ░            ░  ░             ░  ░
        """)

backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Knife
"""

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def backtomenu_option():
        print(backtomenu_banner)
        backtomenu = input("knife > ")

        if backtomenu == "99":
            restart_program()
        elif backtomenu == "0" or backtomenu == "00":
            sys.exit()
        else:
            print("\nERROR: Wrong Input")
            time.sleep(2)
            restart_program()

#Value
today = datetime.today()

#month day year
now = today.strftime("%B %d %Y, %H:%M:%S " + " Have a nice day :)")

#Date Now
print(time.strftime("%Y-%m-%d"))

def start():
    datetz = '2024-10-31'
    expirez = time.strftime("%Y-%m-%d")
    if expirez >= datetz:
        os.system("clear")
        print("Script Expired! Please Update")
        time.sleep(3)
        sys.exit()

def check_status():
#Status Check
    dateted = '2024-10-31'
    expireDate = time.strftime("%Y-%m-%d")
    if expireDate >= dateted:
        print("Status: Expired")
    else:
        print("Status: Running")

#Functions
def num1():
    os.system("clear")
    os.system('ip addr')
    backtomenu_option()

def vulscan():
    ip = input("IP/URL : ")
    os.system("nmap -sV --script=vulscan/vulscan.nse " + ip)
    backtomenu_option()

def vulners():
    ip = input("IP/URL : ")
    os.system("nmap -sV --script=vulners.nse " + ip)
    backtomenu_option()

def dos():
    ip = input("IP/URL : ")
    os.system("nmap --script dos " + ip)
    backtomenu_option()

def num3():
    ip = input("IP/URL : ")
    os.system("nmap " + ip)
    backtomenu_option()

def parameter():
    ip = input("IP/URL : ")
    parameter = input("parameter: ")
    os.system("nmap -p " + parameter + ip)
    backtomenu_option()

def particular():
    print("Example: TCP&particular = 7777,973")
    ip = input("IP/URL : ")
    particular = input("TCP&Particular : ")
    os.system("nmap -p " + particular + ip)
    backtomenu_option()

def range():
    print("Example: range&parameter = 76-973")
    ip = input("IP/URL : ")
    parameter = input("range : ")
    os.system("nmap -p " + parameter + ip)
    backtomenu_option()

def tport():
    print("Example: top-ports = 10")
    ip = input("IP/URL : ")
    tport = input("Tport : ")
    os.system("nmap -top-ports " + tport + ip)
    backtomenu_option()

def multihosts():
    ip = input("IP/URL : ")
    ip2 = input("IP/URL : ")
    ip3 = input("IP/URL : ")
    os.system("nmap " + ip + ip2 + ip3)
    backtomenu_option()

def subnets():
    print("Example : subnets = * ")
    ip = input("IP/URL : ")
    subnets = input("subnets : ")
    os.system("nmap " + ip + .*)
    backtomenu_option()

def fullrange():
    print("Example : full range = 127.0.0.1-255")
    ip = input("IP/URL : ")
    fullrange = input("fullrange : ")
    os.system("nmap " + ip+fullrange)
    backtomenu_option()

def osa():
    osa = input("IP/URL : ")
    os.system('nmap -sV ' + osa)
    backtomenu_option()

def stealth():
    ip = input("IP/URL : ")
    os.system("nmap -sS " + ip)
    backtomenu_option()

def serveral():
    print("Use Top ports to scan")
    ip = input("IP/URL : ")
    serveral = input("Tports : ")
    os.system("nmap -top-ports " + n + tport + ip)
    backtomenu_option()

def ip4():
  p4 = input('IPv4> ')
  os.system('nmap -A ' + p4)
  backtomenu_option()

def ip6():
  p6 = input('IPv6> ')
  os.sytem('nmap -A -6 ' + p6)
  backtomenu_option()

def update():
    os.system("clear")
    os.system("figlet UPDATE!")
    os.system("rm -rf KNIFE")
    os.system("git clone https://github.com/Plague1234/KNIFE")
    os.system('mv KNIFE/knife.py $HOME/KNIFE/')
    time.sleep(2)
    os.system('rm -rf $HOME/KNIFE/core')
    time.sleep(2)
    os.system('mv KNIFE/core $HOME/KNIFE/core')
    time.sleep(2)
    os.system('mv KNIFE/version $HOME/KNIFE/version')
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
    datet = '2024-10-31'

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

