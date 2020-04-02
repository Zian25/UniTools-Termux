# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
import os
import sys
import time
from Zawiencom import *

def FacebookBruteForce():
	update()
	os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce.git")
	os.system("mv Facebook-BruteForce ~")
	cc()
	restart_program()


def Hydra():
	update()
	os.system("pkg install hydra")
	cc()
	restart_program()


def facebookcracker():
	update()
	os.system("git clone https://github.com/Ha3MrX/facebook-cracker.git")
	os.system("mv facebook-cracker ~")
	cc()
	restart_program()


def Instahack():
	update()
	os.system("git clone https://github.com/fuck3erboy/instahack.git")
	os.system("mv instahack ~")
	cc()
	restart_program()

def crunch():
	update()
	os.system("pkg install unstable-repo")
	os.system("pkg install crunch")
	cc()
	restart_program()

def hashcat():
	update()
	os.system("git clone https://github.com/hashcat/hashcat.git")
	os.system("mv hashcat ~")
	cc()
	restart_program()

def BlackHydra():
	update()
	os.system("git clone https://github.com/Gameye98/Black-Hydra.git")
	os.system("mv Black-Hydra ~")
	cc()
	restart_program()

def HashBuster():
	update()
	os.system("git clone https://github.com/s0md3v/Hash-Buster.git")
	os.system("mv Hash-Buster ~")
	cc()
	restart_program()

def Facebom():
	update()
	os.system("git clone https://github.com/Oseid/Facebom.git")
	os.system("mv Facebom ~")
	os.system("pip install requests")
	os.system("pip install mechanize")
	cc()
	restart_program()

def brutespray():
	update()
	os.system("git clone https://github.com/hanshaze/brutespray.git")
	os.system("mv brutespray ~")
	os.system("cd ~/brutespray")
	os.system("pip install -r requirements.txt")
	cc()
	restart_program()


def hyprPulse():
	update()
	os.system("git clone https://github.com/Pure-L0G1C/hyprPulse.git")
	os.system("mv hyprPulse ~")
	os.system("cd ~/hyprPulse")
	os.system("chmod + x install.sh")
	os.system("./install.sh")
	cc()
	restart_program()