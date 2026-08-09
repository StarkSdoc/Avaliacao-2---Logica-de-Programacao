import definicoes as d
d.limpa()
d.cabecalho()

biblioteca=[] #Lista que vai armazenar os livros cadastrados

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE CADASTRO DE LIVROS:
def cadastrar_livro():
    print("\n~~ CADASTRO DE LIVROS: ~~")
    titulo= input("Informe o título do livro: ")
    autor= input("Informe o autor do livro: ")
    ano_de_publicacao= input("Informe o ano de publicação: ")
    codigo= input("Informe o código/ISBN do livro: ")

    #Dicionário que representa as informações do livro
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano_de_publicacao": ano_de_publicacao,
        "codigo": codigo,
        "status": "Disponível"} #Status inicia como disponível, pois quando um novo livro é cadastrado ele
                                #estará automaticamente disponível
    
    biblioteca.append(novo_livro) #Adiciona o dicionário (informações do livro) na lista principal "biblioteca"
    print("Livro cadastrado com sucesso!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE LISTAR LIVROS:
def listar_livros():
    if len(biblioteca)==0:#"len()" foi usado para perguntar ao Python "quantos itens tem dentro da lista?"
        print("Não há nenhum livro cadastrado!")
    else:
        print("\n~~ Os livros disponíveis são: ~~\n")
        for livro in biblioteca:#Vai passar por cada livro na biblioteca e buscar as informações solicitadas
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano de publicação: {livro['ano_de_publicacao']}")
            print(f"Código: {livro['codigo']}")
            print(f"Status: {livro['status']}")
            print("-" * 30)#Vai printar 30 tracinhos para formar uma linha que separe um livro do outro


#--------------------------------------------------------------------------------------------------------------------------------------------------------
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
        listar_livros()
    elif opcao=="5":
        print("Buscar um livro")
    elif opcao=="6":
        print("Ordenar a listagem de livros")
    elif opcao=="7":
        print("Deixando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")  