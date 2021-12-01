# -*- coding: utf-8 -*- 
from modulos.Zawiencom import instalador
import os
import sys
import time
from Zawiencom import *

def SocialFish():
    instalador(url=f"https://github.com/An0nUD4Y/SocialFish.git", name="SocialFish", move=True, installer="None")

def SocialPhish():
    instalador(url=f"https://github.com/xHak9x/SocialPhish.git", name="SocialPhish", move=True, installer="cd ~/SocialPhish && chmod +x socialphish.sh")

def Phisherman():
    instalador(url=f"https://github.com/FDX100/Phisher-man.git", name="Phisher-man", move=True, installer="None")

def shellphish():
    instalador(url=f"https://github.com/thelinuxchoice/shellphish.git", name="shellphish", move=True, installer="cd ~/shellphish && pkg install php && pkg install curl && pkg install python2 && chmod +x shellphish.sh")


def HiddenEye():
	update()
	os.system("pkg install wget")
	os.system("pkg install php")
	os.system("git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git")
	os.system("mv HiddenEye ~")
	os.system("cd ~/HiddenEye")
	os.system("pip3 install -r requirements.txt")
	os.system("pip3 install requests")
	cc()
	restart_program()


def gophish():
    instalador(url=f"https://github.com/gophish/gophish.git", name="gophish", move=True, installer="None")

def TurkSploit():
    instalador(url=f"https://github.com/DoughBoiKush/Turk-Sploit.git", name="Turk-Sploit", move=True, installer="None")

def weeman():
    instalador(url=f"https://github.com/evait-security/weeman.git", name="weeman", move=True, installer="None")

def dnstwist():
    instalador(url=f"https://github.com/elceef/dnstwist.git", name="dnstwist", move=True, installer="None")

def Phlexish():
    instalador(url=f"https://github.com/KnightSec-Official/Phlexish.git", name="Phlexish", move=True, installer="None")

def zphisher():
    instalador(url=f"https://github.com/htr-tech/zphisher", name="zphisher", move=True, installer="cd ~/zphisher && chmod +x zphisher.sh")

def nexphisher():
    instalador(url=f"https://github.com/htr-tech/nexphisher.git", name="nexphisher", move=True, installer="cd ~/nexphisher && bash tmux_setup")

def grabcam():
	instalador(url="https://github.com/noob-hackers/grabcam.git", name="grabcam", installer="pip install lolcat")

def saycheese():
    instalador(url=f"https://github.com/blackc03r/saycheese.git", name="saycheese", move=True, installer="None")

def seeu():
    instalador(url=f"https://github.com/noob-hackers/seeu.git", name="seeu", move=True, installer="cd ~/seeu && termux-setup-storage && pkg install curl -y && pkg install wget -y && pkg install php -y")