Feito por: Sophia De Oliveira Coelho - 2A

+-+-+-+-+ AVALIAÇÃO 2 - LÓGICA DE PROGRAMAÇÃO: SISTEMA DE GERENCIAMENTO DE BIBLIOTECA +-+-+-+-+
Este programa é um sistema desenvolvido para realizar o controle e o gerenciamento de livros de uma biblioteca de forma automatizada. O programa permite cadastrar obras, listar, realizar buscas por título ou autor, registrar empréstimos e devoluções, organizar os livros em ordem alfabética, remover cadastros e salvar todas essas informações permanentemente em um arquivo no formato CSV.

1. ARQUIVO PRINCIPAL (main.py):
Este arquivo é o que guarda todo o programa. É ele que mostra a tela inicial no terminal, exibe o menu com as opções para o usuário escolher o que quer fazer, pega as informações que a pessoa digita e chama as outras funções para fazer o sistema funcionar.


• Função: validar_texto(texto):
Esta função recebe como parâmetro o texto digitado pelo usuário e analisa se o campo não foi deixado em branco.

--> Funcionalidade: Remove todos os espaços vazios das extremidades do texto através do método .strip() e verifica o seu tamanho.

--> Restrição: Retorna False caso o usuário tenha apenas apertado a tecla "enter" ou digitado espaços em branco, impedindo a gravação de dados vazios no sistema.


• Função: validar_autor(autor):
Esta função tem como objetivo verificar se o nome do autor digitado contém apenas caracteres válidos (letras e espaços).

--> Funcionalidade: Utiliza um laço de repetição para percorrer cada caractere da palavra individualmente.

--> Restrição: Se o programa encontrar qualquer número no meio do nome através da verificação .isdigit(), a função retorna False e cancela a operação.


• Função: validar_codigo(codigo):
Esta função é utilizada para garantir que o código ISBN digitado siga o padrão numérico correto de identificação de livros.

--> Funcionalidade: Checa a quantidade exata de caracteres informados pelo usuário.

--> Restrição: Retorna False se o código não possuir exatamente 13 dígitos ou se contiver letras e símbolos misturados na digitação.


• Função: cadastrar_livro():
Esta função solicita as informações de um novo livro e cria um registro para ser armazenado na biblioteca.

--> Funcionalidade: Coleta o título, autor, ano de publicação e código ISBN, criando um dicionário com os dados e definindo o status inicial como "Disponivel".

--> Restrição: Passa todas as entradas pelas funções de validação. Caso o ano seja menor que 1000, maior que o ano atual (2026), ou se os campos de texto estiverem incorretos, o cadastro é cancelado e o usuário retorna ao menu.


• Função: listar_livros():
Esta função é responsável por exibir todos os livros que estão atualmente cadastrados no catálogo do sistema.

--> Funcionalidade: Percorre a lista de livros recuperada do arquivo e imprime na tela o título, autor, ano de publicação, código e o status de cada item.

--> Restrição: Se a lista de livros estiver vazia, o programa exibe uma mensagem informando que não existem registros cadastrados.


• Função: buscar_livro():
Esta função permite ao usuário pesquisar por uma obra específica armazenada no sistema.

--> Funcionalidade: Compara o termo digitado pelo usuário com o título e com o autor dos livros cadastrados, exibindo os resultados encontrados.

--> Restrição: Utiliza a conversão .lower() para ignorar diferenças entre letras maiúsculas e minúsculas na busca. Se o termo estiver em branco ou o livro não for encontrado, uma mensagem de erro é exibida.


• Função: registro_de_emprestimo():
Esta função gerencia a alteração de status de um livro para a saída da biblioteca.

--> Funcionalidade: Localiza a obra pelo título ou pelo código ISBN e altera o seu campo de status de "Disponivel" para "Emprestado".

--> Restrição: Se o livro pesquisado já estiver com o status "Emprestado", o programa impede a operação e avisa que o título não está disponível no momento.


• Função: registro_de_devolucao():
Esta função gerencia a alteração de status de um livro no momento do retorno à biblioteca.

--> Funcionalidade: Localiza a obra pelo título ou pelo código ISBN e altera o seu campo de status de "Emprestado" para "Disponivel".

--> Restrição: Se a obra selecionada já estiver com o status "Disponivel", o programa avisa ao usuário que não é possível realizar a devolução.


• Função: identificar_titulo(livro):
Esta função serve como auxiliar para o processo de ordenação do catálogo.

--> Funcionalidade: Acessa a chave do título dentro do dicionário do livro e converte os caracteres para letras minúsculas.

--> Restrição: É utilizada como chave (key) dentro do método .sort() para evitar que palavras iniciadas com letras maiúsculas e minúsculas sejam ordenadas de forma incorreta.


• Funções Auxiliares de Ordenação:
> identificar_titulo(livro): Retorna o título em letras minúsculas para ordenar alfabeticamente sem erros.
> identificar_autor(livro): Retorna o nome do autor em letras minúsculas para padronizar a ordenação por autor.
> identificar_ano(livro): Converte o ano para um valor inteiro para permitir a ordenação cronológica correta.


• Função: ordenar_livros():
Esta função organiza toda a lista de livros de acordo com o critério escolhido pelo usuário.

--> Funcionalidade: Apresenta um menu secundário onde o usuário pode escolher ordenar por Título (A-Z), Autor (A-Z) ou Ano de Publicação (do mais antigo ao mais recente). Aplica o método .sort() com a chave correspondente e salva a nova sequência no arquivo CSV.

--> Restrição: Não executa a ordenação se o acervo estiver completamente vazio ou se a opção de critério digitada for inválida.


• Função: remover_livro():
Esta função faz a exclusão definitiva do registro de um livro no sistema.

--> Funcionalidade: Procura a obra informada pelo usuário por título ou código, remove o dicionário correspondente da lista e atualiza o arquivo CSV.

--> Restrição: Exige que o termo informado seja válido e avisa o usuário caso o título não seja localizado na biblioteca.


2. MÓDULO DE PERSISTÊNCIA (salvador.py)
O arquivo salvador.py é o responsável por realizar a integração entre a memória do programa e o arquivo de armazenamento permanente (livros.csv).

• Função: adicionar_livro(livro):
Esta função faz a gravação de uma nova linha no arquivo externo.

--> Funcionalidade: Abre o arquivo CSV no modo de adição ("a") e escreve o dicionário do novo livro no final do documento utilizando o csv.DictWriter.

--> Restrição: Não apaga os dados gravados anteriormente no arquivo.


• Função: listar_livros()
Esta função faz a leitura de todas as informações armazenadas no arquivo externo.

--> Funcionalidade: Abre o arquivo CSV no modo de leitura ("r"), converte cada linha gravada de volta em um dicionário Python utilizando o csv.DictReader e retorna uma lista completa.

--> Restrição: Mantém os dados sincronizados com a memória do programa toda vez que o sistema é iniciado ou consultado.


• Função: armazenar_biblioteca(livros)
Esta função atualiza todo o conteúdo do arquivo externo de uma só vez.

--> Funcionalidade: Abre o arquivo CSV no modo de escrita ("w") e sobrescreve todo o documento com a lista de livros atualizada através do comando writerows.

--> Restrição: É utilizada apenas quando ocorrem alterações em dados já existentes, como no empréstimo, devolução, ordenação ou remoção de livros.


3. COMO USAR O SISTEMA:
Para rodar o programa na sua máquina, siga os passos abaixo:

• Pré-requisitos:
--> Possuir o Python 3 instalado no computador.

--> Manter todos os arquivos do projeto (main.py, salvador.py, definicoes.py e livros.csv) salvos dentro da mesma pasta.

• Passo a passo para execução:
+ 1 - Abra a pasta onde os arquivos do projeto estão salvos.
+ 2 - Clique na barra de endereço da pasta, digite "cmd" e aperte Enter para abrir o terminal.
+ 3 - No terminal, digite o comando "python main.py" e aperte Enter para iniciar o sistema.
+ 4 - O sistema exibirá o menu principal na tela com as opções numeradas de 1 a 8.
+ 5 - Digite o número correspondente à função que deseja utilizar (ex: digite 1 para cadastrar ou 4 para listar) e aperte "enter".
+ 6 - Siga as instruções exibidas na tela e insira os dados solicitados. Caso digite alguma informação incorreta, o programa exibirá um aviso de erro e retornará em segurança para o menu inicial.
+ 7 - Para encerrar o programa e salvar todas as alterações com segurança, escolha a opção 8 no menu principal.
