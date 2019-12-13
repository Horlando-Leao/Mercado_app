import os
import platform
import Menu

def consultar_cliente():#retornando soemeten as linhas que posssuem a palavra que eu escolher

    nome = str(input('codigo ou nome: '))
    arq = open('lista_cliente.txt','r')
    contador = 0 #determinar em quantas linhas está o nome desejado

    for linha in arq:
        linha = linha.rstrip()
        if nome in linha: # verificar 
            contador = contador + 1
            print(linha)

    print('\nForam retornados', contador,'resultados')
    arq.close()

    consulta = int(input('1:SIM | 0:NÃO\nFazer nova consulta?'))
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    
    if consulta == 1:
        consultar_cliente()
    else:
        Menu.menu_mercado()

def consultar_produto():#retornando soemeten as linhas que posssuem a palavra que eu escolher

    nome = str(input('Codigo ou nome: '))
    arq = open('lista_produto.txt','r')
    contador = 0 #determinar em quantas linhas está o nome desejado

    for linha in arq:
        linha = linha.rstrip()
        if nome in linha: # verificar 
            contador = contador + 1
            print(linha)

    print('\nForam retornados', contador,'resultados')
    arq.close()

    consulta = int(input('1:SIM | 0:NÃO\nFazer nova consulta?'))
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    
    if consulta == 1:
        consultar_produto()
    else:
        Menu.menu_mercado()
