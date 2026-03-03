#Exercicio 2: Utilizando for


texto = "Hoje é a segunda aula do bootcamp , bootcamp de Python."

palavras = texto.split() #cria uma lista de palavras do texto

print(palavras)

contagem_de_palavras = {} #criando um dicionario vazio para armazenar a contagem de palavras
# quero percorrer todas as palavras dentro de palavras e ver quantas palavras tem

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1