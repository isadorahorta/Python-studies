produto1: str = "sapato"
produto2: str = "camisa"
produto3: str = "videogame"

lista_produtos: list = []

lista_produtos.append(produto1)
lista_produtos.append(produto2)
lista_produtos.append(produto3)

for produto in lista_produtos:
    print(produto)

lista_produtos.pop()
print(lista_produtos)