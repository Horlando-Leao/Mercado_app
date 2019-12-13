import os
import platform
import Menu


def registrar_cliente():

    arquivo = open('lista_cliente.txt','a')

    cpf = str(input('CPF: '))
    nome_cliente = str(input('Nome completo: '))
    n_casa = str(input('numero da casa: '))
    bairro = str(input('bairro: '))
    cidade = str(input('cidade: '))
    telefone = str(input('telefone: '))

    arquivo.write('\nCPF:{}| Nome:{} | Nº casa:{} | Bairro:{} | Cidade:{} | Telofone:{}\n'.format(cpf, nome_cliente, n_casa, bairro, cidade, telefone))
    arquivo.close()
    print('registrado com sucesso')
    
    registrar_novo_cliente = int(input('\nregistar novo cliente?\n1:SIM ou 0:NÃO'))
    os.system('cls') if platform.system()=="Windows" else os.system('clear')

    if registrar_novo_cliente == 1:
        registrar_cliente()
    else:
        Menu.menu_mercado()

def registrar_produto():

    arquivo = open('lista_produto.txt', 'a')

    codigo_produto = str(input('codigo: '))
    nome_produto = str(input('nome do produto: '))
    preco_produto = str(input('preço: '))

    arquivo.write('\nCodigo:{} | Produto:{} | Preço:{}'.format(codigo_produto, nome_produto, preco_produto))
    arquivo.close()
    print('registrado com sucesso')
    
    
    registar = int(input('registar novo produto?\n1:SIM ou 0:NÃO'))
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    
    if registar == 1:
        registrar_produto()
    else:
        Menu.menu_mercado()
        
