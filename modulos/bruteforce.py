# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
from modulos.Zawiencom import instalador
import os
import sys
import time
from Zawiencom import *

def FacebookBruteForce():
    instalador(url=f"https://github.com/IAmBlackHacker/Facebook-BruteForce.git", name="Facebook-BruteForce", move=True, installer="None")


def Hydra():
	update()
	os.system("pkg install hydra")
	cc()
	restart_program()


def facebookcracker():
    instalador(url=f"https://github.com/Ha3MrX/facebook-cracker.git", name="facebook-cracker", move=True, installer="None")


def Instahack():
    instalador(url=f"https://github.com/fuck3erboy/instahack.git", name="Instahack", move=True, installer="None")

def crunch():
	update()
	os.system("pkg install unstable-repo")
	os.system("pkg install crunch")
	cc()
	restart_program()

def hashcat():
    instalador(url=f"https://github.com/hashcat/hashcat.git", name="hashcat", move=True, installer="None")

def BlackHydra():
    instalador(url=f"https://github.com/Gameye98/Black-Hydra.git", name="BlackHydra", move=True, installer="None")

def HashBuster():
    instalador(url=f"https://github.com/s0md3v/Hash-Buster.git", name="Hash-Buster", move=True, installer="None")

def Facebom():
    instalador(url=f"https://github.com/Oseid/Facebom.git", name="Facebom", move=True, installer="cd ~/Facebom && pip install requests && pip install mechanize")

def brutespray():
    instalador(url=f"https://github.com/hanshaze/brutespray.git", name="brutespray", move=True, installer="cd ~/brutespray && pip install -r requirements.txt")


def hyprPulse():
    instalador(url=f"https://github.com/Pure-L0G1C/hyprPulse.git", name="hyprPulse", move=True, installer="cd ~/hyprPulse && chmod + x install.sh && ./install.sh")


def lazybee():
	instalador(url="https://github.com/noob-hackers/lazybee.git", 
	name="lazybee", installer="pkg install python2 -y && pip install lolcat -y")


def Instabruteforce():
    instalador(url=f"https://github.com/Hackertrackersj/Instabruteforce.git", name="Instabruteforce", move=True, installer="cd ~/Instabruteforce && pip install pipenv && pipenv --python 3.9 && pipenv install")


def HackFacebokpass():
    instalador(url=f"https://github.com/lunnar211/HackFacebokpass.git", name="HackFacebokpass", move=True, installer="cd ~/HackFacebokpass && chmod +x * && pip2 install requests && pip2 install mechanize")


