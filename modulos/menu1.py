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
	print ("Digite nmap no terminal para usar!")
	restart_program()

#2
def Th3inspector():
	update()
	os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git")
	os.system("mv Th3inspector ~")
	os.system("cd ~")
	os.system("cd Th3inspector")
	os.system("chmod +x install.sh && ./install.sh")
	cc()
	restart_program()

#3
def angryFuzzer():
	update()
	os.system("git clone https://github.com/ihebski/angryFuzzer.git")
	os.system("mv angryFuzzer ~")
	os.system("cd ~")
	os.system("cd angryFuzzer")
	patch_pip()
	os.system("pip install -r requirements.txt")
	cc()
	restart_program()

#4
def PhoneInfoga():
	update()
	os.system("git clone https://github.com/sundowndev/PhoneInfoga.git")
	os.system("mv PhoneInfoga ~ ")
	os.system("cd ~")
	os.system("cd PhoneInfoga")
	os.system("pip install -r requirements.txt")
	cc()
	restart_program()

def FBI():
	update()
	os.system("git clone https://github.com/KnightSec-Official/FBI.git")
	os.system("mv FBI ~")
	python2_path()
	os.system("cd ~")
	os.system("cd FBI")
	os.system("pip2 install -r requirements.txt")
	cc()
	restart_program()


def Infoga():
	update()
	os.system("git clone https://github.com/m4ll0k/Infoga.git")
	os.system("mv Infoga ~")
	os.system("cd ~")
	os.system("python3 setup.py install")
	cc()
	restart_program()

def InfoSploit():
	update()
	os.system("git clone https://github.com/CybernetiX-S3C/InfoSploit.git")
	os.system("mv InfoSploit ~")
	os.system("cd ~")
	os.system("cd InfoSploit")
	python2_path()
	os.system("chmod +x install")
	os.system("./install")
	cc()
	restart_program()


def BillCipher():
	update()
	os.system("git clone https://github.com/GitHackTools/BillCipher.git")
	os.system("mv BillCipher ~")
	os.system("apt update && apt install ruby python python-pip python3 python3-pip")
	os.system("apt install httrack whatweb")
	os.system("pip install -r requirements.txt")
	os.system("pip3 install -r requirements.txt")
	cc()
	restart_program()


def gasmask():
	update()
	os.system("git clone https://github.com/twelvesec/gasmask.git")
	os.system(" mv gasmask ~")
	os.system("cd ~/gasmask")
	os.system("pip install -r requirements.txt")
	cc()
	restart_program()


def OSIF():
	update()
	os.system("git clone https://github.com/CiKu370/OSIF.git")
	os.system("mv OSIF ~")
	python2_path()
	os.system("cd ~/OSIF")
	path_pip2()
	os.system("pip2 install -r requirements.txt")
	cc()
	restart_program()


def inmux():
	update()
	os.system("git clone https://github.com/Indonesia-Security-Lite/inmux.git")
	os.system("mv inmux ~")
	cc()
	restart_program()


def IPTracer():
	update()
	os.system("git clone https://github.com/Rajkumrdusad/IP-Tracer.git")
	os.system("mv IP-Tracer ~")
	os.system("cd ~")
	os.system("cd IP-Tracer")
	os.system("chmod +x install")
	os.system("sh install")
	cc()
	restart_program()


def RED_HAWK():
	update()
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
	os.system("mv RED_HAWK ~")
	cc()
	restart_program()


def TMscanner():
	update()
	os.system("git clone https://github.com/TechnicalMujeeb/TM-scanner.git")
	os.system("mv TM-scanner ~")
	cc()
	restart_program()


def sqlmx_termux():
	update()
	os.system("git clone https://github.com/CYB3RMX/sqlmx_termux.git")
	os.system("mv sqlmx_termux ~")
	cc()
	restart_program()


def reconspider():
	update()
	os.system("git clone https://github.com/bhavsec/reconspider.git")
	os.system("mv reconspider ~")
	cc()
	restart_program()


def ReconDog():
	update()
	os.system("git clone https://github.com/s0md3v/ReconDog.git")
	os.system("mv ReconDog ~")
	cc()
	restart_program()

def userrecon():
	update()
	os.system("git clone https://github.com/thelinuxchoice/userrecon.git")
	os.system("mv userrecon ~")
	cc()
	restart_program()


def IPGeolocation():
	update()
	os.system("git clone https://github.com/JohnLuca12/IPGeolocation.git")
	os.system("mv IPGeolocation ~")
	cc()
	restart_program()


def OptivaFramework():
	update()
	os.system("git clone https://github.com/joker25000/Optiva-Framework.git")
	os.system("mv Optiva-Framework ~")
	cc()
	restart_program()


def wpscan():
	update()
	os.system("git clone https://github.com/wpscanteam/wpscan.git")
	os.system("mv wpscan ~")
	cc()
	restart_program()


def theHarvester():
	update()
	os.system("git clone https://github.com/laramies/theHarvester.git")
	os.system("mv theHarvester ~")
	cc()
	restart_program()


def KnockMail():
	update()
	os.system("git clone https://github.com/4w4k3/KnockMail.git")
	os.system("mv KnockMail ~")
	cc()
	restart_program()

def SCANNERINURLBR():
	update()
	os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
	os.system("mv SCANNER-INURLBR ~")
	cc()
	restart_program() 

def dmitry():
	update()
	os.system("git clone https://github.com/jaygreig86/dmitry")
	os.system("mv dmitry ~")
	cc()
	restart_program()

def ShodanHat():
	update()
	os.system("git clone https://github.com/HatBashBR/ShodanHat.git")
	os.system("mv ShodanHat ~")
	cc()
	restart_program()

def Hatwitch():
	update()
	os.system("git clone https://github.com/HatBashBR/Hatwitch.git")
	os.system("mv Hatwitch ~")
	cc()
	restart_program()

def URLextractor():
	update()
	os.system("git clone https://github.com/eschultze/URLextractor.git")
	os.system("mv URLextractor ~")
	cc()
	restart_program()

def webkiller():
	update()
	os.system("git clone https://github.com/ultrasecurity/webkiller.git")
	os.system("mv webkiller ~")
	cc()
	restart_program()

def creepy():
	update()
	os.system("git clone https://github.com/ilektrojohn/creepy.git")
	os.system("mv creepy ~")
	cc()
	restart_program()

def seeker():
	update()
	os.system("git clone https://github.com/thewhiteh4t/seeker.git")
	os.system("mv seeker ~")
	os.system("cd seeker")
	os.system("chmod 777 termux_install.sh")
	os.system("./termux_install.sh")
	cc()
	restart_program()



def twifo_cli():
	update()
	os.system("git clone https://github.com/CodeDotJS/twifo-cli.git")
	os.system("mv twifo-cli ~")
	os.system("cd ~/twifo-cli")
	os.system("pkg install nodejs")
	os.system("npm install --global twifo-cli")
	cc()
	restart_program()


def sherlock():
	update()
	os.system("git clone https://github.com/sherlock-project/sherlock.git")
	os.system("mv sherlock ~")
	os.system("cd ~/sherlock")
	os.system("python3 -m pip install -r requirements.txt")
	cc()
	restart_program()

