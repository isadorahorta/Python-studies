#TypeHint

#linguagem dinâmica e forte

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

# Solicita ao usuário que digite seu nome
while nome_valido == False:    
    try:
        nome: str = input("Digite seu nome: ")
            #Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
            #Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
        continue
    
while salario_valido == False:
        try:
            salario:float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor maior que zero para o salário.")
            else:
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

while bonus_valido == False:
    try:
        bonus_recebido:float = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
    #Assumindo valores para a conta
bonus_final: float = bonus_recebido * 1.2  
kpi: float = (salario + bonus_final) / 1000 

    # Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")