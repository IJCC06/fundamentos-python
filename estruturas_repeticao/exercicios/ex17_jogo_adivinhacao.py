def jogo_de_adivinhacao(numero_secreto):
    while True:
        numero = int(input("Faça seu palpite: "))

        if numero < numero_secreto:
            print("É maior!")
        if numero > numero_secreto:
            print("É menor!")
        if numero == numero_secreto:
            print("Número Correto!")
            return 0

jogo_de_adivinhacao(12)