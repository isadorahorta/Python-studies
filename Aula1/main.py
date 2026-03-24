#Programa que recebe o nome, salário e bônus de um funcionário e calcula o salário total

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o valor do bônus: "))
print("Olá, " + nome + ". Seu salário total é de: R$" + str(1000 + salario * bonus) + ".")