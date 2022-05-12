# -*- coding: utf-8 -*-
# Gathering information
import os
import sys
import time
from Zawiencom import *

def nmap():
	update()
	os.system ("apt-get install nmap")
	cc()
	restart_program()

#2
def Th3inspector():
    instalador(url=f"https://github.com/Moham3dRiahi/Th3inspector.git", name="Th3inspector", move=True, installer="cd ~/Th3inspector && chmod +x install.sh && ./install.sh")

#3
def angryFuzzer():
    instalador(url=f"https://github.com/ihebski/angryFuzzer.git", name="angryFuzzer", move=True, installer="cd ~/angryFuzzer && pip install -r requirements.txt")

#4
def PhoneInfoga():
    instalador(url=f"https://github.com/sundowndev/PhoneInfoga.git", name="PhoneInfoga", move=True, installer="cd ~/PhoneInfoga && pip install -r requirements.txt")

def FBI():
    instalador(url=f"https://github.com/KnightSec-Official/FBI.git", name="FBI", move=True, installer="cd ~/FBI && pip2 install -r requirements.txt")


def Infoga():
    instalador(url=f"https://github.com/m4ll0k/Infoga.git", name="Infoga", move=True, installer="cd ~/Infoga && python3 setup.py install")

def InfoSploit():
    instalador(url=f"https://github.com/CybernetiX-S3C/InfoSploit.git", name="InfoSploit", move=True, installer="cd ~/InfoSploit && chmod +x install && ./install")


def BillCipher():
    instalador(url=f"https://github.com/GitHackTools/BillCipher.git", name="BillCipher", move=True, installer="cd ~/BillCipher && apt update && apt install ruby python python-pip python3 python3-pip && apt install httrack whatweb && pip install -r requirements.txt && pip3 install -r requirements.txt")



def gasmask():
    instalador(url=f"https://github.com/twelvesec/gasmask.git", name="gasmask", move=True, installer="cd ~/gasmask && pip install -r requirements.txt")


def OSIF():
    instalador(url=f"https://github.com/CiKu370/OSIF.git", name="OSIF", move=True, installer="cd ~/OSIF && pip2 install -r requirements.txt")


def inmux():
    instalador(url=f"https://github.com/Indonesia-Security-Lite/inmux.git", name="inmux", move=True, installer="None")


def IPTracer():
    instalador(url=f"https://github.com/Rajkumrdusad/IP-Tracer.git", name="IPTracer", move=True, installer="cd ~/IPTracer && chmod +x install && sh install")


def RED_HAWK():
    instalador(url=f"https://github.com/Tuhinshubhra/RED_HAWK.git", name="RED_HAWK", move=True, installer="None")


def TMscanner():
    instalador(url=f"https://github.com/TechnicalMujeeb/TM-scanner.git", name="TMscanner", move=True, installer="None")


def sqlmx_termux():
    instalador(url=f"https://github.com/CYB3RMX/sqlmx_termux.git", name="sqlmx_termux", move=True, installer="None")


def reconspider():
    instalador(url=f"https://github.com/bhavsec/reconspider.git", name="reconspider", move=True, installer="None")


def ReconDog():
    instalador(url=f"https://github.com/s0md3v/ReconDog.git", name="ReconDog", move=True, installer="None")

def userrecon():
    instalador(url=f"https://github.com/thelinuxchoice/userrecon.git", name="userrecon", move=True, installer="None")


def IPGeolocation():
    instalador(url=f"https://github.com/JohnLuca12/IPGeolocation.git", name="IPGeolocation", move=True, installer="None")


def OptivaFramework():
    instalador(url=f"https://github.com/joker25000/Optiva-Framework.git", name="OptivaFramework", move=True, installer="None")


def wpscan():
    instalador(url=f"https://github.com/wpscanteam/wpscan.git", name="wpscan", move=True, installer="None")


def theHarvester():
    instalador(url=f"https://github.com/laramies/theHarvester.git", name="theHarvester", move=True, installer="None")


def KnockMail():
    instalador(url=f"https://github.com/4w4k3/KnockMail.git", name="KnockMail", move=True, installer="None")

def SCANNERINURLBR():
    instalador(url=f"https://github.com/googleinurl/SCANNER-INURLBR.git", name="SCANNER-INURLBR", move=True, installer="None")

def dmitry():
    instalador(url=f"https://github.com/jaygreig86/dmitry.git", name="dmitry", move=True, installer="None")

def ShodanHat():
    instalador(url=f"https://github.com/HatBashBR/ShodanHat.git", name="ShodanHat", move=True, installer="None")

def Hatwitch():
    instalador(url=f"https://github.com/HatBashBR/Hatwitch.git", name="Hatwitch", move=True, installer="None")

def URLextractor():
    instalador(url=f"https://github.com/eschultze/URLextractor.git", name="URLextractor", move=True, installer="None")

def webkiller():
    instalador(url=f"https://github.com/ultrasecurity/webkiller.git", name="webkiller", move=True, installer="None")

def creepy():
    instalador(url=f"https://github.com/ilektrojohn/creepy.git", name="creepy", move=True, installer="None")

def seeker():
    instalador(url=f"https://github.com/thewhiteh4t/seeker.git", name="seeker", move=True, installer="cd ~/seeker && chmod 777 termux_install.sh && ./termux_install.sh")



def twifo_cli():
    instalador(url=f"https://github.com/CodeDotJS/twifo-cli.git", name="twifo-cli", move=True, installer="cd ~/twifo_cli && pkg install nodejs && npm install --global twifo-cli")


def sherlock():
    instalador(url=f"https://github.com/sherlock-project/sherlock.git", name="sherlock", move=True, installer="cd ~/sherlock && python3 -m pip install -r requirements.txt")


def osi_ig():
    instalador(url=f"https://github.com/th3unkn0n/osi.ig.git", name="osi.ig", move=True, installer="None")
