#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

palavra = "banana"

ocorrencias = {} #dicionario vazio

for caractere in palavra:
    if caractere in ocorrencias: #se no meu dicionario eu tenho esse caractere
        ocorrencias[caractere] += 1 #se sim, eu incremento o valor do caractere em 1
    else:
        ocorrencias[caractere] = 1 #senão, fica somente 1

print(ocorrencias)