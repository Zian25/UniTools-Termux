# -*- coding: utf-8 -*-

import sys
sys.path.append("cd ../")
from utx import *
from modulos.Zawiencom import *
from Zawiencom import *
from osint import *
from dos import *
from phishing import *
from exploit import *
from bruteforce import *
from autoinstalador import *
from var_en import *
from var_es import *
from var_pt import *

# Definições de variáveis de idioma

if pt == True:
    backto = "  [00] Voltar para o menu\n"
    choose = "Selecione uma opção: "
    dica1 = dicas_menu1_pt
    dica2 = dicas_menu2_pt

elif en == True:
    backto = "  [00] Back to menu\n"
    choose = "Select an option: "
    dica1 = dicas_menu1_en
    dica2 = dicas_menu2_en

elif es == True:
    backto = "  [00] Volver al menu\n"
    choose = "Seleccione una opción: "
    dica1 = dicas_menu1_es
    dica2 = dicas_menu2_es

else:
    backto = "  [00] Back to menu\n"
    choose = "Select an option: "
    dica1 = dicas_menu1_en
    dica2 = dicas_menu2_en

def osint():
			os.system("clear")
			print ("  [1] Nmap")
			print ("  [2] Th3inspector")
			print ("  [3] angryFuzzer")
			print ("  [4] PhoneInfoga")
			print ("  [5] FBI")
			print ("  [6] Infoga - Email OSINT")
			print ("  [7] InfoSploit")
			print ("  [8] BillCipher")
			print ("  [9] gasmask")
			print ("  [10] OSIF")
			print ("  [11] inmux")
			print ("  [12] IP-Tracer")
			print ("  [13] RED_HAWK")
			print ("  [14] TM-scanner")
			print ("  [15] sqlmx_termux")
			print ("  [16] reconspider")
			print ("  [17] ReconDog")
			print ("  [18] userrecon")
			print ("  [19] IPGeolocation")
			print ("  [20] Optiva-Framework")
			print ("  [21] wpscan")
			print ("  [22] theHarvester")
			print ("  [23] KnockMail")
			print ("  [24] dmitry")
			print ("  [25] ShodanHat")
			print ("  [26] Hatwitch")
			print ("  [27] URLextractor")
			print ("  [28] webkiller")
			print ("  [29] creepy")
			print ("  [30] Seeker")
			print ("  [31] Twifo-cli")
			print ("  [32] Sherlock")
			print ("  [33] osi.ig")
			print ("  [34] Arjun")
			print ("  [35] CloudFail")
			print ("  [36] dnstwist")
			print ("  [37] holehe")
			print ("  [38] pwnedOrNot")
			print (backto)
			print (random.choice(dica1))
			print ("\n")

			#Pergunta da primeira opção de ferramentas
			menu = input(choose)

			if menu == "0" or menu == "00":
				os.system("clear")
				restart_program()

			elif menu == "1" or menu == "01":
				nmap()

			elif menu == "2" or menu == "02":
				Th3inspector()

			elif menu == "3" or menu == "03":
				angryFuzzer()

			elif menu == "4" or menu == "04":
				PhoneInfoga()
				
			elif menu == "5" or menu == "05":
				FBI()
				
			elif menu == "6" or menu == "06":
				Infoga()

			elif menu == "7" or menu == "07":
				InfoSploit()

			elif menu == "8" or menu == "08":
				BillCipher()

			elif menu == "9" or menu == "09":
				gasmask()

			elif menu == "10":
				OSIF()

			elif menu == "11":
				inmux()

			elif menu == "12":
				IPTracer()

			elif menu == "13":
				RED_HAWK()

			elif menu == "14":
				TMscanner()

			elif menu == "15":
				sqlmx_termux()

			elif menu == "16":
				reconspider()

			elif menu == "17":
				ReconDog()

			elif menu == "18":
				userrecon()

			elif menu == "19":
				IPGeolocation()

			elif menu == "20":
				OptivaFramework()

			elif menu == "21":
				wpscan()

			elif menu == "22":
				theHarvester()

			elif menu == "23":
				KnockMail()

			elif menu == "24":
				dmitry()

			elif menu == "25":
				ShodanHat()

			elif menu == "26":
				Hatwitch()

			elif menu == "27":
				URLextractor()

			elif menu == "28":
				webkiller()

			elif menu == "29":
				creepy()

			elif menu == "30":
				seeker()

			elif menu == "31":
				twifo_cli()

			elif menu == "32":
				sherlock()

			elif menu == "33":
				osi_ig()

			elif menu == "34":
				Arjun()

			elif menu == "35":
				CloudFail()

			elif menu == "36":
				dnstwist()		

			elif menu == "37":
				holehe()

			elif menu == "38":
				pwnedOrNot()	

			else:
				erro()

def dos():
			os.system("clear")
			print ("  [1] Xerxes")
			print ("  [2] Slowloris")
			print ("  [3] Hammer")
			print ("  [4] Hunner")
			print ("  [5] GoldenEye")
			print ("  [6] DDos-Attack")
			print ("  [7] Ddoser")
			print ("  [8] torshammer")
			print ("  [9] LITEDDOS")
			print ("  [10] hulk")
			print ("  [11] Memcrashed-DDoS-Exploit")
			print ("  [12] Planetwork-DDOS")
			print ("  [13] Ping_of_death")
			print ("  [14] IcmpiFlood")
			print ("  [15] exploit-blacknurse")
			print ("  [16] PyFlooder")
			print ("  [17] Saddam")
			print ("  [18] ntpdos")
			print (backto)
			print (random.choice(dica2))
			print ("\n")

			menu2 = input(choose)

			if menu2 == "0" or menu2 == "00":
				os.system("clear")
				restart_program()

			elif menu2 == "1" or menu2 == "01":
				xerxes()

			elif menu2 == "2" or menu2 == "02":
				slowloris()

			elif menu2 == "3" or menu2 == "03":
				hammer()

			elif menu2 == "4" or menu2 == "04":
				Hunner()

			elif menu2 == "5" or menu2 == "05":
				GoldenEye()

			elif menu2 == "6" or menu2 == "06":
				DDosAttack()

			elif menu2 == "7" or menu2 == "07":
				Ddoser()

			elif menu2 == "8" or menu2 == "08":
				torshammer()

			elif menu2 == "9" or menu2 == "09":
				LITEDDOS()

			elif menu2 == "10":
				hulk()

			elif menu2 == "11":
				MemcrashedDDoSExploit()

			elif menu2 == "12":
				PlanetworkDDOS()

			elif menu2 == "13":
				ping_of_death()

			elif menu2 == "14":
				IcmpiFlood()

			elif menu2 == "15":
				exploitblacknurse()

			elif menu2 == "16":
				PyFlooder()

			elif menu2 == "17":
				Saddam()

			elif menu2 == "18":
				ntpdos()



			else:
				erro()


def phishing():
			os.system("clear")
			print ("  [1] SocialFish")
			print ("  [2] SocialPhish")
			print ("  [3] Phisher-man")
			print ("  [4] shellphish")
			print ("  [5] HiddenEye")
			print ("  [6] gophish")
			print ("  [7] Turk-Sploit")
			print ("  [8] weeman")
			print ("  [9] dnstwist")
			print ("  [10] Phlexish")
			print ("  [11] zphisher")
			print ("  [12] nexphisher")
			print ("  [13] grabcam")
			print ("  [14] saycheese")
			print ("  [15] seeU")
			print (backto)
			menu3 = input(choose)

			if menu3 == "0" or menu3 == "00":
				os.system("clear")
				restart_program()

			elif menu3 == "1" or menu3 == "01":
				SocialFish()

			elif menu3 == "2" or menu3 == "02":
				SocialPhish()

			elif menu3 == "3" or menu3 == "03":
				Phisherman()

			elif menu3 == "4" or menu3 == "04":
				shellphish()

			elif menu3 == "5" or menu3 == "05":
				HiddenEye()

			elif menu3 == "6" or menu3 == "06":
				gophish()

			elif menu3 == "7" or menu3 == "07":
				TurkSploit()

			elif menu3 == "8" or menu3 == "08":
				weeman()

			elif menu3 == "9" or menu3 == "09":
				dnstwist()

			elif menu3 == "10":
				Phlexish()

			elif menu3 == "11":
				zphisher()

			elif menu3 == "12":
				nexphisher()

			elif menu3 == "13":
				grabcam()
			
			elif menu3 == "14":
				saycheese()

			elif menu3 == "15":
				seeu()

			else:
				erro()



def exploit():
			os.system("clear")
			print ("  [1] XAttacker")
			print ("  [2] routersploit")
			print ("  [3] SVScanner")
			print ("  [4] Revslider-Auto-Exploiter")
			print ("  [5] sqlmap")
			print ("  [6] exploitdb")
			print ("  [7] Pompem")
			print ("  [8] OWScan")
			print ("  [9] sqlscan")
			print ("  [10] D-TECT-1")
			print ("  [11] Striker")
			print ("  [12] SH33LL")
			print ("  [13] Xshell")
			print ("  [14] sqlninja")
			print ("  [15] DirAttack")
			print ("  [16] DirKiller")
			print (backto)
			menu4 = input(choose)

			if menu4 == "0" or menu4 == "00":
				os.system("clear")
				restart_program()

			elif menu4 == "1" or menu4 == "01":
				XAttacker()

			elif menu4 == "2" or menu4 == "02":
				routersploit()

			elif menu4 == "3" or menu4 == "03":
				SVScanner()			

			elif menu4 == "4" or menu4 == "04":
				RevsliderAutoExploiter()

			elif menu4 == "5" or menu4 == "05":
				sqlmap()

			elif menu4 == "6" or menu4 == "06":
				exploitdb()

			elif menu4 == "7" or menu4 == "07":
				Pompem()

			elif menu4 == "8" or menu4 == "08":
				OWScan()

			elif menu4 == "9" or menu4 == "09":
				sqlscan()

			elif menu4 == "10":
				DTECT1()

			elif menu4 == "11":
				Striker()

			elif menu4 == "12":
				SH33LL()

			elif menu4 == "13":
				Xshell()

			elif menu4 == "14":
				sqlninja()

			elif menu4 == "15":
				DirAttack()

			elif menu4 == "16":
				DirKiller()

			else:
				erro()


def bruteforce():
			os.system("clear")
			print ("  [1] Facebook-BruteForce")
			print ("  [2] Hydra ")
			print ("  [3] facebook-cracker")
			print ("  [4] Instahack")
			print ("  [5] crunch (Wordlist gen)")
			print ("  [6] hashcat")
			print ("  [7] Black-Hydra")
			print ("  [8] Hash-Buster")
			print ("  [9] Facebom")
			print ("  [10] brutespray")
			print ("  [11] hyprPulse")
			print ("  [12] Lazybee (Wordlist gen)")
			print ("  [13] Instabruteforce")
			print ("  [14] HackFacebokpass")
			print (backto)

			menu5 = input(choose)

			if menu5 == "0" or menu5 == "00":
				os.system("clear")
				restart_program()

			elif menu5 == "1" or menu5 == "01":
				FacebookBruteForce()

			elif menu5 == "2" or menu5 == "02":
				UniBruteForce()

			elif menu5 == "3" or menu5 == "03":
				Hydra()

			elif menu5 == "4" or menu5 == "04":
				facebookcracker()

			elif menu5 == "5" or menu5 == "05":
				Instahack()

			elif menu5 == "6" or menu5 == "06":
				crunch()

			elif menu5 == "7" or menu5 == "07":
				hashcat()

			elif menu5 == "8" or menu5 == "08":
				BlackHydra()

			elif menu5 == "9" or menu5 == "09":
				HashBuster()

			elif menu5 == "10":
				Facebom()

			elif menu5 == "11":
				hyprPulse()

			elif menu5 == "12":
				lazybee()

			elif menu5 == "13":
				Instabruteforce()

			elif menu5 == "14":
				HackFacebokpass()

			else:
				erro()


def autoinstall():
	os.system("clear")
	print ("  [1] Metasploit")
	print ("  [2] Sudo su")
	print ("  [3] Nethunter")
	print (vermelho + "  [4] Routersploit" + branco)
	print ("  [5] Nginx")
	print (vermelho + "  [6] Ngrok" + branco)
	print (backto)

	menu6 = input(choose)

	if menu6 == "0" or menu6 == "00":
		os.system("clear")
		restart_program()

	elif menu6 == "1" or menu6 == "01":
		metasploit()

	elif menu6 == "2" or menu6 == "02":
		sudo()

	elif menu6 == "3" or menu6 == "03":
		Nethunter()

	elif menu6 == "4" or menu6 == "04":
		routersploit()

	elif menu6 == "5" or menu6 == "05":
		nginx()

	elif menu6 == "6" or menu6 == "06":
		ngrok()

	else:
		erro()

def pedido_7_pt():
	os.system("clear")
	print ("Em breve...\n")
	print("O que vai ser?")
	print("Um terminal com funções diversificadas Ex: Exploits/Scanners, webscanners. Terminal tudo em um para pentesters!\n")
	print("Quando?")
	print("Até o momento não há uma data especifica\n")
	input("Aperte algo para voltar: ")
	restart_program()


def upToDate():
	os.system("clear")
	print ("Verificando...")
	att()
	restart_program()