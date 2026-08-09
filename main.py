biblioteca=[] #Lista que vai armazenar os livros cadastrados

#FUNÇÃO DE CADASTRO DE LIVROS:
def cadastrar_livro():
    print("\n~~ CADASTRO DE LIVROS: ~~")
    titulo= input("Informe o título do livro: ")
    autor= input("Informe o autor do livro: ")
    ano_de_publicacao= input("Informe o ano de publicação: ")
    codigo= input("Informe o código/ISBN do livro: ")

    #Dicionário que representa as informações do livro
    novo_livro = {
        "título": titulo,
        "autor": autor,
        "ano de publicação": ano_de_publicacao,
        "código": codigo,
        "status": "Disponível"} #Status inicia como disponível, pois quando um novo livro é cadastrado ele
                                #estará automaticamente disponível
    
    biblioteca.append(novo_livro) #Adiciona o dicionário (informações do livro) na lista principal "biblioteca"
    print("Livro cadastrado com sucesso!")

#MENU DE OPÇÕES:
#Apresenta o menu principal com as opções possíveis
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
        cadastrar_livro()
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