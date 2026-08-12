import csv #Importa o módulo csv para conseguir manipular e salvar arquivos .csv no Python
import os #Importa o módulo os para verificar se o arquivo csv já existe na pasta

campos = ["titulo", "autor", "ano_de_publicacao", "codigo", "status"]

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE ADICIONAR UM LIVRO NO CSV:
def adicionar_livro(livro):
    #Verifica se o arquivo "livros.csv" já existe antes de abrir
    arquivo_existe = os.path.exists("livros.csv")

    #O "open" no modo "a" (append) é usado para adicionar uma nova linha no final do arquivo sem apagar os livros que já estavam lá
    with open("livros.csv", "a", newline="", encoding="utf-8") as arquivo: 
        #O "DictWriter" define os nomes das colunas do CSV para corresponderem exatamente às chaves do nosso dicionário
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        
        #Se o arquivo não existia, escreve a primeira linha com o cabeçalho (nomes das colunas)
        if not arquivo_existe:
            escritor.writeheader()
            
        escritor.writerow(livro) #Escreve a linha com os dados do novo livro dentro do arquivo csv

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE LER E LISTAR OS LIVROS DO CSV:
def listar_livros():
    livros = [] #Cria uma lista vazia para guardar todos os livros que forem lidos do arquivo
    
    #Se o arquivo livros.csv ainda não existir na pasta, retorna a lista vazia sem dar erro no programa
    if not os.path.exists("livros.csv"):
        return livros

    #O modo "r" (read) é usado para abrir e ler as informações que já estão salvas no arquivo csv
    with open("livros.csv", "r", newline="", encoding="utf-8") as arquivo: 
        #O "DictReader" vai ler cada linha do arquivo CSV e transformar de volta em um dicionário em Python usando o cabeçalho
        leitor = csv.DictReader(arquivo)
        for livro in leitor: #Vai passar por cada livro lido dentro do leitor
            livros.append(livro.copy()) #O ".append" é usado para adicionar uma cópia do dicionário do livro dentro da nossa lista "livros"
            
    return livros #Entrega a lista completa de livros para a def que chamou a função

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÃO DE REESCREVER/ATUALIZAR O ARQUIVO CSV COMPLETO:
def armazenar_biblioteca(livros):
    #O modo "w" (write) é usado para sobrescrever/atualizar todo o arquivo CSV do zero (usado após remoção, empréstimo, devolução ou ordenação)
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo: 
        #O "DictWriter" organiza o cabeçalho e os nomes das colunas no arquivo csv
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader() #Garante que o cabeçalho com o nome das colunas continue no topo do arquivo
        escritor.writerows(livros) #O "writerows" escreve a lista inteira de livros atualizada de uma vez só no arquivo csv