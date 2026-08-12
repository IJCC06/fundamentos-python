def analise_eleitores():
    idade = int(input("Digite sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade == 16 or idade == 17:
        print("Voto Opcional")
    elif 18 <= idade <= 69:
        print("Voto Obrigatório")
    elif idade >= 70:
        print("Voto Opcional")
    else:
        print("Idade Inválida")

analise_eleitores()