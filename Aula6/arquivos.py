#python tem um módulo de csv
import csv

#path
caminho_arquivo: str = "exemplo.csv" #caminho do arquivo
    
arquivo_csv :list = [] #criando uma lista vazia, para fazer uma lista de dicionários

#with é um gerenciador de contexto, ele garante que o arquivo seja fechado mesmo que haja um erro
with open(file = caminho_arquivo, mode="r", encoding="utf-8") as arquivo: 
    leitor_csv = csv.DictReader(arquivo) #DictReader lê o arquivo csv linha por linha e tranforma cada linha em um dicionário

    for linha in leitor_csv: #percorre cada linha do arquivo csv
        arquivo_csv.append(linha) #adiciona cada linha na lista arquivo_csv

print(arquivo_csv)