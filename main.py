from etl import ler_csv, filtrar_produtos_entregues, somar_valores_produtos_entregues

## Projeto02-Python

#Desafio: Análise de Vendas de Produtos 
# Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, 
# processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.



path_arquivo = r"C:\Users\rates\OneDrive\Documentos\Estudos_Python\Projeto02-Python\vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
valor_total_produtos_entregues = somar_valores_produtos_entregues(produtos_entregues)


print(valor_total_produtos_entregues)