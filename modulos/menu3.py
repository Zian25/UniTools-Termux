# -*- coding: utf-8 -*- 
import os
import sys
import time
from Zawiencom import *

def SocialFish():
	update()
	os.system("git clone https://github.com/An0nUD4Y/SocialFish.git")
	os.system("mv SocialFish ~")
	cc()
	restart_program()


def SocialPhish():
	update()
	os.system("git clone https://github.com/xHak9x/SocialPhish.git")
	os.system("mv SocialPhish ~")
	os.system("cd ~/SocialPhish")
	os.system("chmod +x socialphish.sh")
	cc()
	restart_program()


def Phisherman():
	update()
	os.system("git clone https://github.com/FDX100/Phisher-man.git")
	os.system("mv Phisher-man ~")
	cc()
	restart_program()


def shellphish():
	update()
	os.system("pkg install python2")
	os.system("pkg install php")
	os.system("pkg install curl")
	os.system("git clone https://github.com/thelinuxchoice/shellphish.git")
	os.system("mv shellphish ~")
	os.system("cd shellphish")
	os.system("chmod +x shellphish.sh")
	cc()
	restart_program()


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
	update()
	os.system("git clone https://github.com/gophish/gophish.git")
	os.system("mv gophish ~")
	cc()
	restart_program()


def TurkSploit():
	update()
	os.system("git clone https://github.com/DoughBoiKush/Turk-Sploit.git")
	os.system("mv Turk-Sploit ~")
	cc()
	restart_program()

def weeman():
	update()
	os.system("git clone https://github.com/evait-security/weeman.git")
	os.system("mv weeman ~")
	cc()
	restart_program()

def dnstwist():
	update()
	os.system("git clone https://github.com/elceef/dnstwist.git")
	os.system("mv dnstwist ~")
	cc()
	restart_program()

def Phlexish():
	update()
	os.system("git clone https://github.com/KnightSec-Official/Phlexish.git")
	os.system("mv Phlexish ~")
	cc()
	restart_program()


def zphisher():
	update()
	#os.system("apt-get install git php openssh curl -y")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("mv zphisher ~")
	os.system("cd ~/zphisher")
	os.system("chmod +x zphisher.sh")
	cc()
	restart_program()


def nexphisher():
	update()
	os.system("git clone https://github.com/htr-tech/nexphisher.git")
	os.system("mv nexphisher ~")
	os.system("cd ~/nexphisher")
	os.system("bash tmux_setup")
	cc()
	restart_program()