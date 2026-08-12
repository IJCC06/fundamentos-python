def precificador_ingresso():
    idade = int(input("Digite a idade: "))

    if idade <= 5:
        print("Gratuito")
    elif 6 <= idade <= 12:
        print("R$ 10,00")
    elif 13 <= idade <= 59:
        print("R$ 20,00")
    elif idade >= 60:
        print("R$ 10,00")

precificador_ingresso()