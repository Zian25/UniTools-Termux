# -*- coding: utf-8 -*-
import os

#def instalador(url=None, name=None, move=True, installer=None):
#	update()
#	if url != None:
#		os.system(f"git clone {url}")
#
#	if move != False:
#		os.system(f"mv {name} ~")
#
#	if installer != None:
#		os.system(f"cd ~/{name}")
#		os.system(installer)


def main():
    name = input("Digite o nome da ferramenta: ")
    github = input("Link Github: ")
    instalador = input("Instalador: ")

    if name == None:
        print("Nome incorreto")
        exit(1)

    if github == None:
        print("Github não informado")
        exit(1)
    
    if instalador != "":
        instalador = f"cd ~/{name} && {instalador}"
    
    else:
        instalador = None
    
    gerador = f'''
def {name}():
    instalador(url=f"{github}", name="{name}", move=True, installer="{instalador}")
    '''
    
    print(gerador)
    
    repetir = input("Repetir?: ")
    if repetir == "s" or repetir == "sim":
        os.system("clear")
        main()
    else:
        exit(0)


if __name__ == "__main__":
    os.system("clear")
    main()