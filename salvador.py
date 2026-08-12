import csv
def adicionar_livro(livro):
    with open("livros.csv","a", newline="", encoding="utf-8") as arquivo: 
        escritor=csv.DictWriter(arquivo, fieldnames=["titulo", "autor", "ano_de_publicacao","codigo","status"])
        escritor.writerow(livro)

def listar_livros():
    livros=[]
    with open("livros.csv","r", newline="", encoding="utf-8") as arquivo: 
        leitor=csv.DictReader(arquivo, fieldnames=["titulo", "autor", "ano_de_publicacao","codigo","status"])
        for livro in leitor:
            livros.append(livro.copy())
    return livros

def armazenar_biblioteca(livros):
    with open("livros.csv","w", newline="", encoding="utf-8") as arquivo: 
        escritor=csv.DictWriter(arquivo, fieldnames=["titulo", "autor", "ano_de_publicacao","codigo","status"])
        escritor.writerows(livros)
