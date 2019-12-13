import os
import platform
import Query
import Record
import Update
import Delete

def menu_mercado():
    print('CLIENTE:______________________________________________________ \n      1:RESGISTAR | 2:CONSULTAR | 3:ATUALIZAR | 4:DELETAR\n' )
    print('PRODUTO:______________________________________________________ \n      5:RESGISTAR | 6:CONSULTAR | 7:ATUALIZAR | 8:DELETAR\n' )
    print('                      0:FECHAR PROGRAMA')
    
    menu = int(input('\nOPÇÃO: '))
    os.system('cls') if platform.system()=="Windows" else os.system('clear')

    if menu == 1:
        Record.registrar_cliente()
    elif menu == 2 :
        Query.consultar_cliente()
    elif menu == 3 :
        print('updadte do cliente: ainda em desenvolvimento')
    elif menu == 4:
        print('delete do cliente: ainda em desenvolvimento')
    elif menu == 5:
        Record.registrar_produto()
    elif menu == 6 :
        Query.consultar_produto()
    elif menu == 7 :
        print('updadte do produto: ainda em desenvolvimento')
    elif menu == 8:
        print('delete do produto: ainda em desenvolvimento')
    elif menu == 0 :
        print('programa finalizado')
    else:
        os.system('cls') if platform.system()=="Windows" else os.system('clear')

        print('essa opção não existe, digite uma opção valida')
        menu_mercado()

print('DESEJA ENTRAR NO PROGRAMA?')
x= int(input('1:SIM | 0: NÃO...:'))
os.system('cls') if platform.system()=="Windows" else os.system('clear')
if x == 1:
    menu_mercado()
else:
    print('Até mais seu lerdo!')
