def conversao_idade():
    idade_anos = int(input("Digite sua idade: "))
    idade_meses = idade_anos * 12
    idade_dias = idade_meses * 365
    print(f"Você tem {idade_anos} anos ou {idade_meses} meses ou {idade_dias} dias")

conversao_idade()