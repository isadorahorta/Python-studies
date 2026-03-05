import json


produto_01: dict = {
    "nome": "sapato",
    "quantidade": 10,
    "preco": 150.00,
    "disponivel": True

}

produto_02: dict = {
    "nome": "camisa",
    "quantidade": 20,
    "preco": 80.00, 
    "disponivel": True
}

carrinho :list = [] #criando uma lista vazia de carrinho de compras

carrinho.append(produto_01) #adicionando o produto 01 ao carrinho
carrinho.append(produto_02) #adicionando o produto 02 ao carr

print(carrinho)

carrinho_json = json.dumps(carrinho) #convertendo a lista de carrinho para formato JSON
print(carrinho_json)



produto_01["preco"] = 120.00
print(produto_01)

#se a chave não existir, ela é criada
produto_01["cor"] = "preto"
print(produto_01)

for chave in produto_01:
    if chave == "nome" and chave in produto_01:
        print("Existe")

    else:
        print("Não existe")

livro = {
    "titulo":'O Senhor dos Anéis',
    "autor":'J.R.R. Tolkien',
    "ano_publicacao":1954,
}

lista_elementos_livro = livro.items() #retorna uma lista de tuplas contendo as chaves e valores do dicionário
for elemento in lista_elementos_livro:
    print(elemento)