# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
import os
import sys
import time
import re
import subprocess
vermelho = '\033[31m'
branco = '\033[37m'
verde = '\033[32m'


#Banner 
def banner():
	print ("                    #     # ####### #     # " )
	print ("                    #     #    #     #   #  " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #       #    " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #     #   #  " )
	print ("                     #####     #    #     #   v0.1.3" )

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

def instalador(url=None, name=None, move=True, installer=None):
	update()
	if url != None:
		os.system(f"git clone {url}")

	if move != False:
		os.system(f"mv {name} ~")

	if installer != None or installer != "None":
		os.system(f"cd ~/{name}")
		os.system(installer)

	cc()
	restart_program()

	pass

def erro_en():
	os.system("clear")
	print ("OPS! It seems that you inserted an incorrect option :(")
	time.sleep(3)
	os.system("clear")
	restart_program()

def erro_es():
	os.system("clear")
	print ("OPS! Parece que has insertado una opción incorrecta :(")
	time.sleep(3)
	os.system("clear")
	restart_program()


def cc():
	os.system("clear")
	print ("Concluido!")
	time.sleep(3)
def update():
	os.system("pkg update -y && pkg upgrade -y")

def root():
	print ("Root é necessario")
	print ("Deseja continuar?" + verde + "(S)im" + vermelho +"(N)ão" + branco)
	pedido_root = input("Selecione uma opção: ")
	if pedido_root == "S" or pedido_root == "s" or pedido_root == "Sim" or pedido_root == "sim":
		pass
	else:
		restart_program()

def root_en():
	print ("Root is required")
	print ("Do you wish to continue?" + verde + "(Y)es" + vermelho +"(N)o" + branco)
	pedido_root = input("Selecione uma opção: ")
	if pedido_root == "Y" or pedido_root == "y" or pedido_root == "Yes" or pedido_root == "yes":
		pass
	else:
		restart_program()



def root_es():
	print ("La raíz es necesaria (Root)")
	print ("¿Desea continuar?" + verde + "(S)í" + vermelho +"(N)o" + branco)
	pedido_root = input("Selecione uma opção: ")
	if pedido_root == "S" or pedido_root == "s" or pedido_root == "Si" or pedido_root == "si" or pedido_root == "sí" or pedido_root == "Sí":
		pass
	else:
		restart_program()
		