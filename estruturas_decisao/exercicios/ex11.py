def calculadora_imc():
    peso = round(float(input("Digite seu peso em kg: ")), 1)
    altura = float(input("Digite a altura em m: "))
    imc = round(peso / (altura ** 2), 1)

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso Normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
    else:
        print("Algum número tá errado, bichão")

calculadora_imc()