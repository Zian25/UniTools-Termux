# -*- coding: utf-8 -*-
import sys
sys.path.append("modulos")
from Zawiencom import *

#Inicio do script (Menu)
def main():
	try:
		os.system("clear")
		banner()
		print ("          [1] Ferramentas de coleta de informaçôes")
		print ("          [2] Ferramentas de DoS")
		print ("          [3] Ferramentas de Phishing")
		print ("          [4] Ferramentas de Exploração (Exploit)(Scanners)")
		print ("          [5] Ferramentas de Brute-force")
		print ("          [6] Pacotes e Utilidades & Auto-Instaladores")
		print ("          [7] Procurar atualização (UniTools-Termux)")
		print ("          [X] Sair")
		print ("                 ")
		pedido = input("Selecione uma opçâo: ")

		if pedido == "1":
			os.system("clear")
			print ("          [1] Nmap")
			print ("          [2] Th3inspector")
			print ("          [3] angryFuzzer")
			print ("          [4] PhoneInfoga")
			print ("          [5] FBI")
			print ("          [6] Infoga - Email OSINT")
			print ("          [7] InfoSploit")
			print ("          [8] BillCipher")
			print ("          [9] gasmask")
			print ("          [10] OSIF")
			print ("          [11] inmux")
			print ("          [12] IP-Tracer")
			print ("          [13] RED_HAWK")
			print ("          [14] TM-scanner")
			print ("          [15] sqlmx_termux")
			print ("          [16] reconspider")
			print ("          [17] ReconDog")
			print ("          [18] userrecon")
			print ("          [19] IPGeolocation")
			print ("          [20] Optiva-Framework")
			print ("          [21] wpscan")
			print ("          [22] theHarvester")
			print ("          [23] KnockMail")
			print ("          [00] Para Voltar")
			print ("          ")

			#Pergunta da primeira opção de ferramentas
			menu = input("Selecione uma opção: ")

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

			else:
				erro()


			# Fim do primeiro menu de instalação

		# Começo do 2 menu de instalação

		if pedido == "2" or pedido == "02":
			os.system("clear")
			print ("          [1] Xerxes")
			print ("          [2] Slowloris")
			print ("          [3] Hammer")
			print ("          [4] Hunner")
			print ("          [5] GoldenEye")
			print ("          [6] DDos-Attack")
			print ("          [7] Ddoser")
			print ("          [8] torshammer")
			print ("          [9] LITEDDOS")
			print ("          [10] hulk")
			print ("          [11] Memcrashed-DDoS-Exploit")
			print ("          [00] Sair do menu de instalação")
			print ("                ")

			menu2 = input("Selecione uma opção: ")

			if menu2 == "0" or menu2 == "00":
				os.system("clear")
				restart_program()

			elif menu2 == "1" or menu2 == "01":
				xerxes()

			elif menu2 == "2" or menu == "02":
				slowloris()

			elif menu2 == "3" or menu == "03":
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

			else:
				erro()


		# Fim do 2 menu de instalação

		# Começo do 3 menu de instalação
		if pedido == "3" or pedido == "03":
			os.system("clear")
			print ("          [1] SocialFish")
			print ("          [2] SocialPhish")
			print ("          [3] Phisher-man")
			print ("          [4] shellphish")
			print ("          [5] Umbrella")
			print ("          [6] HiddenEye")
			print ("          [7] gophish")
			print ("          [8] Turk-Sploit")
			print ("          [00] Sair para o menu")
			print ("         ")
			menu3 = input("Selecione uma opção: ")

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
				Umbrella()

			elif menu3 == "6" or menu3 == "06":
				HiddenEye()

			elif menu3 == "7" or menu3 == "07":
				gophish()

			elif menu3 == "8" or menu3 == "08":
				TurkSploit()

			else:
				erro()

		# Fim do 3 menu de instalação
		if pedido == "4" or pedido == "04":
			os.system("clear")
			print ("          [1] XAttacker")
			print ("          [2] routersploit")
			print ("          [3] SVScanner")
			print ("          [4] Revslider-Auto-Exploiter")
			print ("          [5] sqlmap")
			print ("          [6] exploitdb")
			print ("          [7] Pompem")
			print ("          [8] OWScan")
			print ("          [9] sqlscan")
			print ("          [10] D-TECT-1")
			print ("          [11] Striker")
			print ("          [12] SH33LL")
			print ("          [13] Xshell")
			print ("          [00] Para sair para o menu")
			print ("                  ")
			menu4 = input("Selecione uma opção: ")

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


			else:
				erro()

		# Fim do 4 menu de instalação

		# Começo do 5 menu de instalação

		if pedido == "5" or pedido == "05":
			os.system("clear")
			print ("          [1] Facebook-BruteForce")
			print ("          [2] UniBrute-Force")
			print ("          [3] Hydra ")
			print ("          [4] facebook-cracker")
			print ("          [5] Instahack")
			print ("          [6] crunch")
			print ("          [7] hashcat")
			print ("          [8] Black-Hydra")
			print ("          [00] Para sair para o menu")
			print ("       ")

			menu5 = input("Selecione uma opção: ")

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

			else:
				os.system("clear")
				print ("OPS! Parece que você inseriu uma opção incorreta :(")
				time.sleep(4)
				restart_program()
			# Fim do 5 menu de instalação

		if pedido == "6" or pedido == "06":
			os.system("clear")
			print ("          [1] Metasploit")
			print ("          [00] Sair para o menu ")
			print ("       ")

			menu6 = input("Selecione uma opção: ")

			if menu6 == "0" or menu6 == "06":
				os.system("clear")
				restart_program()

			elif menu6 == "1" or menu6 == "01":
				metasploit()

			else:
				erro()

		if pedido == "7" or pedido == "07":
			os.system("clear")
			print ("Verificando...")
			att()
			restart_program()

		if pedido == "x" or pedido == "X":
			os.system("clear")
			os.system("exit")

		else:
			erro()

	except KeyboardInterrupt:
		os.system("clear")
		print ("\nSaindo...")
		time.sleep(1)
		os.system("clear")

main()