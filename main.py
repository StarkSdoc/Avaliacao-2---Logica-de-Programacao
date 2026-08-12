import definicoes as d
d.limpa()
d.cabecalho()

import salvador as s #Chama as defs do arquivo "salvador" para exportar as atualizações para o arquivo csv

#Função para evitar que o usuário digite apenas "enter" sem por uma informação de verdade
def validar_texto(texto): #Recebe o texto digitado pelo usuário
    if len(texto.strip()) == 0: #Remove espaços e verifica se ficou vazio
        return False #Retorna False se o usuário só apertou "enter" ou digitou espaços
    return True #Retorna True se o texto for válido


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE CADASTRO DE LIVROS:
def validar_autor(autor): #def para verificar se existem números no nome do autor
    for letra in autor:
        if letra.isdigit(): #Se houver números no nome do autor, o programa vai retornar "False"
            return False

    return True #Se o loop acima verificar que não há números em "autor", o programa vai retornar "True"

def validar_codigo(codigo):
    if len(codigo) != 13:#Se o código for diferente do que 13 digitos, ou seja, com mais ou menos digitos, o programa vai enviar uma mensagem de invalidez e irá retornar para o menu principal
        return False
    if codigo.isdigit() == False:#.isdigit é usado para analisar se o codigo foi escrito somente com números. Se tiver sido
        return False             #escrito com letras, o programa deverá printar uma mensagem de erro e retornar para o menu de opções

    return True #Se o loop acima verificar que não há números em "código", o programa vai retornar "True"


def cadastrar_livro():
    #Mensagem de cabeçalho e boas vindas
    print("\n+-+-+-+-+-+- CADASTRO DE LIVROS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de cadastro!")
    #Pede que usuário digite o título e autor do livro e salva essas informações nas variáveis "titulo" e "autor"
    titulo= input("Informe o título do livro: ")

    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(titulo) == False:
        print("\n ⨻ O título não pode ficar em branco. Tente novamente. ⨻")
        return

    autor= input("Informe o autor do livro: ")
    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(autor) == False:
        print("\n ⨻ O nome do autor não pode ficar em branco. Tente novamente. ⨻")
        return
    #if para verificar se o nome do autor foi escrito corretamente (sem números)
    if validar_autor(autor) == False:
        print("\n⨻ O nome do autor foi escrito incorretamente. Tente novamente. ⨻")
        return

    ano_de_publicacao= input("Informe o ano de publicação: ") #Solicita o ano de publicação da obra
    if ano_de_publicacao.isdigit()==False:#.isdigit é usado para analisar se o ano foi escrito somente com números. Se tiver sido
                                            #escrito com letras, o programa deverá printar uma mensagem de erro e retornar para o menu de opções
        print("\n ⨻ Esta data está incorreta. Tente novamente. ⨻")
        return

    if int(ano_de_publicacao)>2026 or int(ano_de_publicacao)<1000: #Se a data for depois do ano atual (2026) o programa irá exibir uma mensagem de invalidez e irá retornar para o menu principal
        print("\n ⨻ Esta data está incorreta. Tente novamente. ⨻")
        return

    codigo= input("Informe o código/ISBN do livro: ") #Solicita o código ISBN
    if validar_codigo(codigo)==False:
        print("\n ⨻ Este código não é tolerado. Tente novamente. ⨻")
        return

    novo_livro = {#Dicionário que representa as informações do livro
        "titulo": titulo ,
        "autor": autor ,
        "ano_de_publicacao": ano_de_publicacao ,
        "codigo":codigo ,
        "status": "Disponivel"} #Status inicia como disponível, pois quando um novo livro é cadastrado ele
                                #estará automaticamente disponível

    s.adicionar_livro(novo_livro) #Adiciona o dicionário (informações do livro) na lista principal "biblioteca"
    print("Livro cadastrado com sucesso!")


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE LISTAR LIVROS:
def listar_livros():
    biblioteca = s.listar_livros()
    print("\n+-+-+-+-+-+- LISTAGEM DE LIVROS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de listagem!")
    if len(biblioteca)==0:#"len()" foi usado para perguntar ao Python "quantos itens tem dentro da lista?"
        print("⨻ Não há nenhum livro cadastrado! ⨻")
    else:
        print("\n~~ Os livros em catálogo são: ~~\n")
        for livro in biblioteca:#Vai passar por cada livro na biblioteca e buscar as informações solicitadas
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano de publicação: {livro['ano_de_publicacao']}")
            print(f"Código: {livro['codigo']}")
            print(f"Status: {livro['status']}")
            print("-" * 30)#Vai printar 30 tracinhos para formar uma linha que separe um livro do outro


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE BUSCAR LIVROS:
def buscar_livro():
    biblioteca= s.listar_livros()
    print("\n+-+-+-+-+-+- BUSCA DE LIVROS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de busca!")
    termo=input("Informe o livro ou autor que deseja encontrar: ")#Guardou a resposta do usuário em "termo" para usar como a chave da pesquisa

    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(termo) == False:
        print("\n ⨻ A pesquisa não pode ficar em branco. Tente novamente. ⨻")
        return

    encontrou = False #Variável para saber se achamos o livro ou não
    #Pede para o usuário informar o título de uma obra, ou um autor, para que o programa procure entre todos os livros cadastrados na biblioteca
    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro["autor"].lower():
        #".lower" foi usado para que o programa não bug caso o livro tenha sido registrado com letra maiúscula e o usuário tenha digitado com letra minúscula e vice-versa
        #Assim, o ".lower" vai deixar tudo em letra minúscula e programa vai rodar normalmente
            print(f"\nLivro encontrado: {livro['titulo']} - Autor: {livro['autor']}")
            print(f"Status: {livro['status']}")
            print("-" * 30)
            encontrou = True #A variável passa a ser verdadeira pois o programa rodou por todos os livros e encontrou aquele que estava sendo procurado

    if encontrou == False:
            print("⨻ Nenhum livro ou autor encontrado. Tente novamente. ⨻")
        #Isso só aparece caso o programa não encontre o livro/autor. A variável "encontrou" vai continuar como False e então a mensagem deste print deverá aparecer indicando que a busca fracassou.

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE REGISTRO DE EMPRÉSTIMOS:
def registro_de_emprestimo():
    biblioteca= s.listar_livros()
    print("\n+-+-+-+-+-+- REGISTRO DE EMPRÉSTIMOS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de empréstimo!")
    #Usa a mesma estrutura da busca de livros para que o usuário possa procurar por código ou título
    termo=input("Digite o código ou nome do livro que deseja pegar: ")

    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(termo) == False:
        print("\n ⨻ O código ou título não pode ser vazio. Tente novamente. ⨻")
        return

    encontrou=False
    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['codigo'].lower():
            encontrou = True #Caso o livro seja encontrado entre os já cadastrados, o programa abaixo irá rodar
            if livro['status'] == "Disponivel":
                livro['status']="Emprestado"
            #Caso o status atual do livro selecionado para empréstimo seja "Disponível", o programa mudará para "Emprestado"
                print(f"\n O livro '{livro['titulo']}' foi emprestado a você. Aproveite a leitura!")
            else:
                print(f"Sentimos muito, o livro {livro['titulo']} já foi emprestado a alguém! Aguarde a devolução.")
            #Se ao selecionar o livro o status dele já for "Emprestado" o programa irá avisar ao usuário que o empréstimo não é possível
            break #O programa para
    if encontrou==False:
        print("⨻ Não foi possível achar esse título em nossa prateleira. Código ou título não correspondente, tente novamente. ⨻")
    #Caso o livro não tiver sido encontrado, o programa irá enviar essa mensagem
    s.armazenar_biblioteca(biblioteca)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE DEVOLUÇÃO:
#Segue a mesma lógica do registro de empréstimo
def registro_de_devolucao():
    biblioteca= s.listar_livros()
    print("\n+-+-+-+-+-+- REGISTRO DE DEVOLUÇÃO: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de devolução!")
    #Usa a mesma estrutura da busca de livros para que o usuário possa procurar por código ou título
    termo=input("Digite o código ou nome do livro que deseja devolver: ")

    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(termo) == False:
        print("\n ⨻ O código ou título não pode ser vazio. Tente novamente. ⨻")
        return

    encontrou=False
    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['codigo'].lower():
            encontrou = True #Caso o livro seja encontrado entre os já cadastrados, o programa abaixo irá rodar
            if livro['status'] == "Emprestado":
                livro['status']="Disponivel"
            #Caso o status atual do livro selecionado para devolução seja "Emprestado", o programa mudará para "Disponível"
                print(f"\n O livro '{livro['titulo']}' foi devolvido às prateleiras. Obrigada(o)!")
            else:
                print(f"O livro {livro['titulo']} já está disponível. Não é possível fazer a devolução.")
            #Se ao selecionar o livro o status dele já for "Disponível" o programa irá avisar ao usuário que a devolução não é possível
            break #O programa para
    if encontrou==False:
        print("⨻ Não foi possível achar esse título em nossa prateleira. Código ou título não correspondente, tente novamente. ⨻")
    #Caso o livro não tiver sido encontrado, o programa irá enviar essa mensagem
    s.armazenar_biblioteca(biblioteca)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE ORDENAR LIVROS (por título):
def identificar_titulo(livro): #Função que identifica o título do livro e entrega para o ".sort"
    return livro['titulo'].lower()#.lower para que as letra maiúsculas e minúsculas não se embaralhem e o programa trave

def ordenar_livros():
    biblioteca= s.listar_livros()
    print("\n+-+-+-+-+-+- ORDENAGEM DE LIVROS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de ordenagem!")
    if len(biblioteca)==0: #Verifica se há livros na biblioteca, se não houver nenhum livro o programa irá enviar a mensagem abaixo
        print("⨻ Não há livros a serem ordenados. Digite 1 e cadastre novos livros. ⨻")
    else:
        biblioteca.sort(key=identificar_titulo)
        #O .sort vai servir para ordenar os títulos em ordem alfabética. Com ajuda da def acima
        #ele vai "pegar" os livros, identificar o título e por em ordem alfabética.
        print("\nA biblioteca foi organizada por títulos em ordem alfabética. Digite 4 e verifique a nova ordem.")
    s.armazenar_biblioteca(biblioteca)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE REMOVER LIVROS:
def remover_livro():
    biblioteca= s.listar_livros()
    print("\n+-+-+-+-+-+- REMOÇÃO DE LIVROS: -+-+-+-+-+-+")
    print("\nBem vindo(a) a função de remoção!")
    #Usa a mesma estrutura da busca de livros para que o usuário possa procurar por código ou título
    termo=input("Digite o código ou nome do livro que deseja remover: ")

    #Chamando a def de validar texto para garantir que a pessoa não deixe o espaço em branco
    if validar_texto(termo) == False:
        print("\n ⨻ O código ou título não pode ser vazio. Tente novamente. ⨻")
        return
    
    encontrou=False

    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['codigo'].lower():
            encontrou = True #Caso o livro seja encontrado entre os já cadastrados, o programa abaixo irá rodar
            biblioteca.remove(livro)
            s.armazenar_biblioteca(biblioteca)
            print("O livro selecionado foi removido com sucesso! Digite 4 no menu principal e veja a nova lista.")
            break
    if encontrou==False:
        print("⨻ Não foi possível achar esse título em nossa prateleira. Código ou título não correspondente, tente novamente. ⨻")
            #Caso o livro não tiver sido encontrado, o programa irá enviar essa mensagem


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#MENU DE OPÇÕES:
#Apresenta o menu principal com as opções possíveis
while True:#While para manter o menu ativo até que o usuário decida sair
    print("\n--------------------------------------------------SISTEMA DE GERENCIAMENTO DE BIBLIOTECA--------------------------------------------------")
    print("Bem vindo(a) ao sistema de gerenciamento da biblioteca!")
    print("\nPara continuar no programa, digite a opção que mais lhe agrada:")
    print("-- 1 para: Cadastrar livros")
    print("-- 2 para: Registrar empréstimos")
    print("-- 3 para: Registrar devolução")
    print("-- 4 para: Listar todos os livros")
    print("-- 5 para: Buscar um livro")
    print("-- 6 para: Ordenar a listagem de livros")
    print("-- 7 para: Remover livro cadastrado")
    print("-- 8 para: Sair do sistema")

    opcao= input("\nDigite sua opção: ")

    if opcao=="1":
        cadastrar_livro()
    elif opcao=="2":
        registro_de_emprestimo()
    elif opcao=="3":
        registro_de_devolucao()
    elif opcao=="4":
        listar_livros()
    elif opcao=="5":
        buscar_livro()
    elif opcao=="6":
        ordenar_livros()
    elif opcao=="7":
        remover_livro()
    elif opcao=="8":
        print("Deixando o sistema...")
        break
    else:
        print("⨻ Opção inválida, tente novamente. ⨻")