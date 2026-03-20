# Funções em python
def printar_mensagem():
    print("Printar mensagem.")

def printar_mensagem_parametro(mensagem):
    print(mensagem)


printar_mensagem()

printar_mensagem_parametro("oi")

def soma_de_numeros(num1, num2) -> float:
    num3 = num1+num2
    return num3



soma = soma_de_numeros(4,5)
print(soma)
