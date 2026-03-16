from estoquefuncoes import (cadVendas, cadProdutos, abrirBanco, criarTabelas, limparTela)

criarTabelas(abrirBanco())

while True:
    print('=' * 60)
    print("1 - Cadastro de Produtos")
    print("2 - Cadastro de Vendas")
    print('.' * 60)
    print("S - Sair do Sistema")
    print('=' * 60)
    opcao = input("Informe uma das opções acima: ").upper().strip()
    limparTela()
    match (opcao):
        case '1':
            cadProdutos()
        case '2':
            cadVendas()
        case 'S':
            exit()
        
