def caixa_eletronico():
    saldo = float(input("Digite seu saldo: "))
    saque = float(input("Digite o valor do saque: "))

    if saque > saldo:
        print("Saldo Insuficiente")
    elif saque <= 0:
        print("Valor de Saque Inválido")
    else:
        saldo = saldo - saque
        print("Saque Efetuado!")
        print(f"Saldo Atual: R$ {saldo}")

caixa_eletronico()