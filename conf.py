import sys
from utx import *
def conf():
	os.system("clear")
	if pt == True:
		print ("Configuração\n")
		print ("  [1] Mudar idioma")
		print ("  [2] Voltar ao menu\n")

		configura = input("Selecione uma opção: ")

		if configura == "1" or configura == "01":
			os.system("clear")
			print (" [1] Português")
			print (" [2] English")
			print (" [3] Español\n")
			dec = input("Selecione: ")

			if dec == "1" or dec == "01":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace('pt', 'pt')

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()

			if dec == "2" or dec == "02":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("pt", "en")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()



			if dec == "3" or dec == "03":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("pt", "es")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()


		if configura == "2" or configura == "02":
			restart_program()


	if es == True:
		print ("Configuración\n")
		print ("  [1] Cambiar el idioma")
		print ("  [2] Regresar al menú\n")

		configura = input("Seleccione una opción: ")

		if configura == "1" or configura == "01":
			os.system("clear")
			print (" [1] Português")
			print (" [2] English")
			print (" [3] Español\n")
			dec = input("Selecione: ")

			if dec == "1" or dec == "01":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace('es', 'pt')

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()

			if dec == "2" or dec == "02":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("es", "en")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()



			if dec == "3" or dec == "03":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("es", "es")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()


		if configura == "2" or configura == "02":
			restart_program()

	if en == True:
		print ("Settings\n")
		print ("  [1] Change language")
		print ("  [2] Back to menu\n")

		configura = input("Choose an option: ")

		if configura == "1" or configura == "01":
			os.system("clear")
			print (" [1] Português")
			print (" [2] English")
			print (" [3] Español\n")
			dec = input("Selecione: ")

			if dec == "1" or dec == "01":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace('en', 'pt')

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()

			if dec == "2" or dec == "02":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("en", "en")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()



			if dec == "3" or dec == "03":
				f = open("modulos/idioma.txt", "r")
				filedata = f.read()
				f.close()
				repor = filedata.replace("en", "es")

				f = open("modulos/idioma.txt", "w")
				f.write(repor)
				f.close()
				restart_program()

		if configura == "2" or configura == "02":
			restart_program()





