def aprovacao():
    nota = float(input("Digite sua nota: "))

    if 6 <= nota <= 10:
        print("Aprovado")
    elif 0 <= nota < 6:
        print("Reprovado")
    else:
        print("Digite um nota certa, seu idiota!")

aprovacao()