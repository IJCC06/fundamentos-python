def temperatura():
    temperatura = round(float(input("Digite a temperatura: ")), 1)

    if temperatura <= 15:
        print("Frio")
    elif 15 < temperatura <= 25:
        print("Agradável")
    elif temperatura > 25:
        print("Quente")

temperatura()