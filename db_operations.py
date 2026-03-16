import sqlite3 as sql
from stringSQL import (comandoSQL, )
import os

def acessarBanco (sql: str, *variaveis):
	conexao = abrirBanco ( )
	cursor = conexao.cursor ( )
	cursor.execute (sql, tuple (variaveis, ) if variaveis else '')
	conexao.commit( )
	return (conexao, cursor)

def limparTela ( ):
	os.system ("cls")

def abrirBanco ( ):
	conexao = sql.connect ("Estoque.db")
	return conexao 

def criarTabelas (conexao):
	cursor = conexao.cursor( )
	cursor.execute(comandoSQL[0])
	cursor.execute(comandoSQL[1])

def addProduto ( ):
	nome = input ('Informe o Nome do Produto : ').upper( ).strip( )
	descricao = input('Informe a Descrição do Produto: ').upper( ).strip( )
	preco = float( input('Informe o Preço do Produto: '))
	qtEstoque = int (input('Informe a Quantidade do Produto em Estoque: '))
	conn, cursor = acessarBanco ( comandoSQL [2],  nome, descricao, preco, qtEstoque)

def relProduto ( ):
	conn, cursor = acessarBanco (comandoSQL[3])
	listaProdutos = cursor.fetchall( )
	for produto in listaProdutos:
            print("ID:", produto[0])
            print("Nome:", produto[1])
            print("Descrição:", produto[2])
            print("Preço:", produto[3])
            print("Quantidade Disponível:", produto[4])
            print("-"*30)

def addVenda ( ):
	print('-' * 40)
	relProduto( )
	print('-' * 40)
	produtoID = int(input('Informe o Código do Produto vendido: '))
	qtVenda = int(input('Informe a quantidade de Produtos vendido: '))
	data = input('Informe a data da venda(YYYY-MM-DD): ') #precisa formata a dada para sql 
	conn, cursor = acessarBanco (comandoSQL [4], produtoID)
	qtDisponivel = cursor.fetchone()[0]
	if qtVenda <= qtDisponivel:
		conn, cursor = acessarBanco (comandoSQL [5], produtoID, qtVenda, data)
		#Atualização do Estoque:
		conn, cursor = acessarBanco(comandoSQL[6], qtVenda, produtoID)
		print("Venda registrada com sucesso!")
	else:
		print("Venda não realizda. Quantidade vendida maior que a quantidade disponível em estoque.")


def updateProduto ( ):
	print('-' * 40)
	relProduto( )
	print('-' * 40)
	produtoID = int(input('Informe o Código do Produto que deseja atualizar: '))
	opcao = input (' Digite o que deseja atualizar do produto : \n1. Nome \n2. Descrição \n3. Preço \n4.Quantidade em Estoque. \n Para cancelar atualização digite "0"\n').upper().strip()
	while True:
		if opcao == '0':
			break
		if opcao == '1':
			nome = input ('Informe o Novo Nome do Produto : ').upper( ).strip( )
			conn, cursor = acessarBanco(comandoSQL[7], nome, produtoID)
			return
		elif opcao == '2':
			descricao = input('Informe a Nova Descrição do Produto ; ').upper( ).strip( )
			conn, cursor = acessarBanco(comandoSQL[8], descricao, produtoID)
			return
		elif opcao == '3':
			preco = float( input('Informe o Novo Preço do Produto: '))
			conn, cursor = acessarBanco(comandoSQL[9], preco, produtoID)
			return
		elif opcao == '4':
			qtEsto = int( input('Informe a Nova Quantidade do Produto em Estoque: '))
			conn, cursor = acessarBanco(comandoSQL[10], qtEsto, produtoID)
			return
		else:
			print("Opção inválida. ")
			return


def relVendasEstoque( ):
	conn, cursor = acessarBanco (comandoSQL[11])
	relatorio = cursor.fetchall()
	if relatorio:
		for linha in relatorio:
			print("ID do Produto:", linha[0])
			print("Nome do Produto:", linha[1])
			print("Descrição do Produto:", linha[2])
			print("Preço:", linha[3])
			print("Quantidade Disponível:", linha[4])
			print("Quantidade Vendida:", linha[5])
			print("Data da Venda:", linha[6])
			print("-" *10)
	else:
		print("Não há produtos cadastrados.")


def estoque( menu: dict):
    while True:
        print('=' * 60)
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao[0]}")       
        print('=' * 60)
        opcao = input("Informe uma das opções acima: ").upper().strip()
        if opcao.upper() == 'R': break
        eval( menu[opcao][1])


def cadProdutos():
    menu = {
        '1': ["Adicionar produto.", "addProduto()"],
        '2': ["Visualizar todo os produtos disponíveis em estoque.", "relProduto()"],
        '3': ["Atualizar algum produto em estoque.", "updateProduto()"],
        'R': ["Retornar ao Menu Principal", ''],
    }
    estoque(menu)

def cadVendas():
    menu = {
        '1': ["Inclusão de Venda.", "addVenda()"],
        '2': ["Relatório de Estoque.", "relVendasEstoque()"],
        'R': ["Retornar ao Menu Principal", ''],
    }
    estoque(menu)
