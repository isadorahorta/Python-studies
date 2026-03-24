import csv

path_arquivo = r"C:\Users\rates\OneDrive\Documentos\Estudos_Python\Desafio\vendas.csv"

# Função para ler arquivo csv e retornar uma lista de dicionários com esses dados
def ler_csv(path_arquivo: str) -> list[dict]:

    lista = []
    with open(path_arquivo, mode='r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
        return lista


#Função que filtra produtos que entregue=True
def filtrar_produtos_entregues(produtos: list[dict]) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produto in produtos:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    
    return lista_com_produtos_filtrados

#Função para somar valores de produtos entregues
def somar_valores_produtos_entregues(produtos: list[dict]) -> int:
    valor_total = 0
    for produto in produtos:
        valor_total += int(produto.get("price"))
    
    return valor_total

