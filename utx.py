# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] < 3:
    print ("Python 2 não é suportado, use Python 3!")
    exit(0)

import random
import re
sys.path.append("modulos")
from Zawiencom import *
from osint import *
from dos import *
from phishing import *
from exploit import *
from bruteforce import *
from autoinstalador import *
from conf import *


idioma = open("modulos/idioma.txt", "r+")
leitor = idioma.readlines()
analisa = len(leitor)
if not analisa:
	print ("[01] Português-Brasil")
	print ("[02] Español")
	print ("[03] English\n")
	print ("Select a language")
	lingua_seleciona = input("Selecione uma linguagem: ")
	if lingua_seleciona == "01" or lingua_seleciona == "1":
		idioma.write("pt")
		idioma.close()
		restart_program()
		pass

	elif lingua_seleciona == "02" or lingua_seleciona == "2":
		idioma.write("es")
		idioma.close()
		restart_program()
		pass

	elif lingua_seleciona == "03" or lingua_seleciona == "3":
		idioma.write("en")
		idioma.close()
		restart_program()
		pass

	else:
		os.system("clear")
		print ("Não foi selecionado uma opção correta, definindo para Português-Brasil")
		print ("No se seleccionó una opción correcta, estableciéndose como portugués-brasileño")
		print ("A correct option was not selected, setting to Portuguese-Brazilian\n")
		print ("Altere essa linguagem nas configurações")
		print ("Cambie este idioma en los ajustes")
		print ("Change this language in the settings")
		time.sleep(5)
		idioma.write("pt")
		idioma.close()
		restart_program()

pt = False
en = False
es = False
pt_check = "pt"
en_check = "en"
es_check = "es"

from var_pt import *
from var_en import *
from var_es import *

with open("modulos/idioma.txt", "r") as a:
	for linha in a:
		if pt_check.lower() == linha.lower().strip():
			pt = True
			#from var_pt import *
			pass
		elif en_check.lower() == linha.lower().strip():
			en = True
			#from var_en import *
			pass

		elif es_check.lower() == linha.lower().strip():
			es = True
			#from var_es import *
			pass

from swaplanguage import *

#Inicio do script (Menu)
def main():
	try:

		if pt == True:
			os.system("clear")
			banner()
			print ("\n")
			print ("  [1] Ferramentas de coleta de informaçôes")
			print ("  [2] Ferramentas de DoS")
			print ("  [3] Ferramentas de Phishing")
			print ("  [4] Ferramentas de Exploração (Exploit)(Scanners)")
			print ("  [5] Ferramentas de Brute-force")
			print ("  [6] Outros (Instaladores & Utilidades)")
			print ( vermelho + "  [7] ZawieSole - Beta" + branco)
			print ("  [8] Configurações")
			print ("  [9] Procurar atualização (UniTools-Termux)")
			print ("  [X] Sair\n")
			print (random.choice(dicas_pt_init))
			print("\n")
			pedido = input("Selecione uma opçâo: ")
			os.system("clear")

			if pedido == "1" or pedido == "01":
				osint()

			elif pedido == "2" or pedido == "02":
				dos()

			elif pedido == "3" or pedido == "03":
				phishing()

			elif pedido == "4" or pedido == "04":
				exploit()

			elif pedido == "5" or pedido == "05":
				bruteforce()

			elif pedido == "6" or pedido == "06":
				autoinstall()

			elif pedido == "7" or pedido == "07":
				pedido_7_pt()

			elif pedido == "8" or pedido == "08":
				conf()

			elif pedido == "9" or pedido == "09":
				att()

			elif pedido.lower() == "x" or pedido.lower() == "xx":
				os.system("clear")
				print ("\nSaindo...")
				sys.exit()

			else:
				erro()


		elif en == True:
			os.system("clear")
			banner()
			print ("\n")
			print("  [1] Gathering Information")
			print("  [2] Stress (DoS) ") 
			print("  [3] Phishing (Attack of credentials)")
			print("  [4] Exploit & Scanners")
			print("  [5] Brute-force")
			print("  [6] Others (Installers and Utilities)")
			print(vermelho + "  [7] ZawieSole - Beta" + branco)
			print("  [8] Settings")
			print("  [9] Search update (UniTools-Termux)")
			print("  [X] Exit\n")
			print (random.choice(dicas_en_init))
			print("\n")
			pedido = input("Select an option: ")
			if pedido == "1" or pedido == "01":
				osint()

			elif pedido == "2" or pedido == "02":
				dos()

			elif pedido == "3" or pedido == "03":
				phishing()

			elif pedido == "4" or pedido == "04":
				exploit()

			elif pedido == "5" or pedido == "05":
				bruteforce()

			elif pedido == "6" or pedido == "06":
				autoinstall()

			elif pedido == "7" or pedido == "07":
				pedido_7_pt()

			elif pedido == "8" or pedido == "08":
				conf()

			elif pedido == "9" or pedido == "09":
				att()

			elif pedido.lower() == "x" or pedido.lower() == "xx":
				os.system("clear")
				print ("\nLeaving...")
				sys.exit()


			else:
				erro_en()



		elif es == True:
			os.system("clear")
			banner()
			print ("\n")
			print("  [1] Recopilación de información")
			print("  [2] Estrés (DoS) ") 
			print("  [3] Phishing (Ataque de credenciales)")
			print("  [4] Exploit & Scanners")
			print("  [5] Fuerza bruta")
			print("  [6] Otros (Instaladores y Utilidades)")
			print(vermelho + "  [7] ZawieSole - Beta" + branco)
			print("  [8] Configuración")
			print("  [9] Buscar actualización (UniTools-Termux)")
			print("  [X] Salir\n")
			print (random.choice(dicas_es_init))
			print ("\n")
			pedido = input("Seleccione una opción: ")
			if pedido == "1" or pedido == "01":
				osint()

			elif pedido == "2" or pedido == "02":
				dos()

			elif pedido == "3" or pedido == "03":
				phishing()

			elif pedido == "4" or pedido == "04":
				exploit()

			elif pedido == "5" or pedido == "05":
				bruteforce()

			elif pedido == "6" or pedido == "06":
				autoinstall()

			elif pedido == "7" or pedido == "07":
				pedido_7_pt()

			elif pedido == "8" or pedido == "08":
				conf()

			elif pedido == "9" or pedido == "09":
				att()

			elif pedido.lower() == "x" or pedido.lower() == "xx":
				os.system("clear")
				print ("\nSaliendo...")
				sys.exit()


			else:
				erro_es()



	except KeyboardInterrupt:
		os.system("clear")
		print ("Saindo...")
		idioma.close()
		time.sleep(1)
		os.system("clear")

def att():
	os.system("clear")
	checker = os.popen("git pull").read()
	if re.search("Already up to date.", checker):
		if pt == True:
			print ("Não há atualizações.")
			time.sleep(4)
			restart_program()

	
		elif es == True:
			print ("No hay actualizaciones.")
			time.sleep(4)
			restart_program()

		elif en == True:
			print ("No updates.")
			time.sleep(4)
			restart_program()

		else:
			print("Não foi possivel determinar seu idioma...")
			time.sleep(4)
			restart_program()

	else:

		if pt == True:
			print ("Atualização disponivel!")
			time.sleep(4)
			restart_program()

		elif es == True:
			print ("Actualización disponible!")
			time.sleep(4)
			restart_program()

		elif en == True:
			print ("Update available!")
			time.sleep(4)
			restart_program()

		else:
			print("Não foi possivel determinar...")
			time.sleep(4)
			restart_program()


if __name__ == "__main__":
	main()

