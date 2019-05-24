# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
import os
import sys
import time

#Banner 
def banner():
	print ("-" * 59)
	print ("                    #     # ####### #     # " )
	print ("                    #     #    #     #   #  " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #       #    " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #     #   #  " )
	print ("                     #####     #    #     #   v1" )
	print ("-" * 59)

# Reiniciar Programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

# Utilidades para facilitar
def erro():
	os.system("clear")
	print ("OPS! Parece que você inseriu uma opção incorreta :(")
	time.sleep(3)
	os.system("clear")
	restart_program()

def cc():
	os.system("clear")
	print ("Concluido!")
	time.sleep(3)
def update():
	os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade -y")

# Fim das Utilidades

# Inicio dos 1 instaladores
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
	cc()
	restart_program()

#3
def angryFuzzer():
	update()
	os.system("git clone https://github.com/ihebski/angryFuzzer.git")
	os.system("mv angryFuzzer ~")
	cc()
	restart_program()

#4
def PhoneInfoga():
	update()
	os.system("git clone https://github.com/sundowndev/PhoneInfoga.git")
	os.system("mv PhoneInfoga ~ ")
	cc()
	restart_program()

def FBI():
	update()
	os.system("")
	os.system("")
	cc()
	restart_program()


def Infoga():
	update()
	os.system("git clone https://github.com/m4ll0k/Infoga.git")
	os.system("mv Infoga ~")
	cc()
	restart_program()

def InfoSploit():
	update()
	os.system("git clone https://github.com/CybernetiX-S3C/InfoSploit.git")
	os.system("mv InfoSploit ~")
	cc()
	restart_program()


def BillCipher():
	update()
	os.system("git clone https://github.com/GitHackTools/BillCipher.git")
	os.system("mv BillCipher ~")
	cc()
	restart_program()


def gasmask():
	update()
	os.system("git clone https://github.com/twelvesec/gasmask.git")
	os.system(" mv gasmask ~")
	cc()
	restart_program()


def OSIF():
	update()
	os.system("git clone https://github.com/CiKu370/OSIF.git")
	os.system("mv OSIF ~")
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


# Fim do Primeiro menu de instalação

# Começo do segundo menu de instalação

def xerxes():
	update()
	os.system("git clone https://github.com/4w4k3/KnockMail.git")
	os.system("mv KnockMail ~")
	cc()
	restart_program()


def slowloris():
	update()
	os.system("git clone https://github.com/llaera/slowloris.pl.git")
	os.system("mv slowloris.pl ~")
	cc()
	restart_program()

def hammer():
	update()
	os.system("git clone https://github.com/cyweb/hammer.git")
	os.system("mv hammer ~")
	cc()
	restart_program()


def Hunner():
	update()
	os.system("git clone https://github.com/b3-v3r/Hunner.git")
	os.system("mv Hunner ~")
	cc()
	restart_program()

def GoldenEye():
	update()
	os.system("git clone https://github.com/jseidl/GoldenEye.git")
	os.system("mv GoldenEye ~")
	cc()
	restart_program()

def DDosAttack():
	update()
	os.system("git clone https://github.com/Ha3MrX/DDos-Attack.git")
	os.system("mv DDos-Attack ~")
	cc()
	restart_program()

def Ddoser():
	update()
	os.system("git clone https://github.com/ZonePy/Ddoser.git")
	os.system("mv Ddoser ~")
	cc()
	restart_program()

def torshammer():
	update()
	os.system("git clone https://github.com/dotfighter/torshammer.git")
	os.system("mv torshammer ~")
	cc()
	restart_program()

def LITEDDOS():
	update()
	os.system("git clone https://github.com/4L13199/LITEDDOS.git")
	os.system("mv LITEDDOS ~")
	cc()
	restart_program()


def hulk():
	update()
	os.system("git clone https://github.com/grafov/hulk.git")
	os.system("mv hulk ~")
	cc()
	restart_program()

def MemcrashedDDoSExploit():
	update()
	os.system("git clone https://github.com/649/Memcrashed-DDoS-Exploit.git")
	os.system("mv Memcrashed-DDoS-Exploit ~")
	cc()
	restart_program()

# Fim do 2 menu de instalação

# Inicio do 3 menu de instalação

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
	os.system("git clone https://github.com/thelinuxchoice/shellphish.git")
	os.system("mv shellphish ~")
	cc()
	restart_program()


def Umbrella():
	update()
	os.system("git clone https://github.com/4w4k3/Umbrella.git")
	os.system("mv Umbrella ~")
	cc()
	restart_program()


def HiddenEye():
	update()
	os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye.git")
	os.system("mv HiddenEye ~")
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

# Fim do 3 menu de instalação

# Inicio do 4 menu de instalação

def XAttacker():
	update()
	os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git")
	os.system("mv XAttacker ~")
	cc()
	restart_program()


def routersploit():
	update()
	os.system("git clone https://github.com/threat9/routersploit.git")
	os.system("mv routersploit ~")
	cc()
	restart_program()


def SVScanner():
	update()
	os.system("git clone https://github.com/radenvodka/SVScanner.git")
	os.system("mv SVScanner ~")
	cc()
	restart_program()

def RevsliderAutoExploiter():
	update()
	os.system("git clone https://github.com/kyuoko/Revslider-Auto-Exploiter.git")
	os.system("mv Revslider-Auto-Exploiter ~")
	cc()
	restart_program()


def sqlmap():
	update()
	os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
	os.system("mv sqlmap ~")
	cc()
	restart_program()


def exploitdb():
	update() 
	os.system("git clone https://github.com/offensive-security/exploitdb.git")
	os.system("mv exploitdb ~")
	cc()
	restart_program()


def Pompem():
	update()
	os.system("git clone https://github.com/rfunix/Pompem.git")
	os.system("mv Pompem ~")
	cc()
	restart_program()


def OWScan():
	update()
	os.system("git clone https://github.com/Gameye98/OWScan.git")
	os.system("mv OWScan ~")
	cc()
	restart_program()


def sqlscan():
	update()
	os.system("git clone https://github.com/Cvar1984/sqlscan.git")
	os.system("mv sqlscan ~")
	cc()
	restart_program()

def DTECT1():
	update()
	os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git")
	os.system("mv D-TECT-1 ~")
	cc()
	restart_program()


def Striker():
	update()
	os.system("git clone https://github.com/s0md3v/Striker.git")
	os.system("mv Striker ~")
	cc()
	restart_program()


def SH33LL():
	update()
	os.system("git clone https://github.com/LOoLzeC/SH33LL.git")
	os.system("mv SH33LL ~")
	cc()
	restart_program()


def Xshell():
	update()
	os.system("git clone https://github.com/Manisso/Xshell.git")
	os.system("mv Xshell ~")
	cc()
	restart_program()

# Fim do 4 menu de instalação

# Inicio do 5 menu de instalação
# Brute-force

def FacebookBruteForce():
	update()
	os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce.git")
	os.system("mv Facebook-BruteForce ~")
	cc()
	restart_program()


def UniBruteForce():
	update()
	os.system("git clone https://github.com/Unizaf/UniBrute-Force.git")
	os.system("mv UniBrute-Force ~")
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
	os.system("git clone https://github.com/crunchsec/crunch.git")
	os.system("mv crunch ~")
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

# Fim do 5 menu de instalação

def metasploit():
	update()
	os.system("cd ~")
	os.system("pkg install wget")
	os.system("wget https://Auxilus.github.io/metasploit.sh")
	os.system("cd metasploit")
	os.system("bash metasploit.sh")
	os.system("./msfconsole")
	cc()
	restart_program()

# Fim do 5 menu de instalação

# Inicio da opção de atualização

def att():
	os.system("git pull")