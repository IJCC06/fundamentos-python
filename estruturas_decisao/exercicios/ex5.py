def classificacao_nota():
    nota = float(input("Digite uma nota: "))

    if 0 <= nota <= 4.9:
        print("Insuficiente")
    elif 5 <= nota <= 6.9:
        print("Regular")
    elif 7 <= nota <= 8.9:
        print("Bom")
    elif 9 <= nota <= 10:
        print("Excelente!")

classificacao_nota()