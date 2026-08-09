#MENU DE OPÇÕES:
#Apresenta o menu principal com as opções possíveis
biblioteca=[] #Lista que vai armazenar os livros cadastrados

while True:#While para manter o menu ativo até que o usuário decida sair
    print("\n~~ SISTEMA DE GERENCIAMENTO DE BIBLIOTECA: ~~")
    print("\nDigite:")
    print("1 para: Cadastrar livros")
    print("2 para: Registrar empréstimos")
    print("3 para: Registrar devolução")
    print("4 para: Listar todos os livros")
    print("5 para: Buscar um livro")
    print("6 para: Ordenar a listagem de livros")
    print("7 para: Sair do sistema")

    opcao= input("\nDigite sua opção: ")

    if opcao=="1":
        print("Cadastrar livros")
    elif opcao=="2":
        print("Registrar empréstimos")
    elif opcao=="3":
        print("Registrar devolução")
    elif opcao=="4":
        print("Listar todos os livros")
    elif opcao=="5":
        print("Buscar um livro")
    elif opcao=="6":
        print("Ordenar a listagem de livros")
    elif opcao=="7":
        print("Deixando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")
    