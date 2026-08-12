def calculadora():
    numero1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o sinal do operador: ")
    numero2 = float(input("Digite o segundo número: "))

    if operador == "+":
        total = numero1 + numero2
        print(f"{numero1} + {numero2} = {total}")
    elif operador == "-":
        total = numero1 - numero2
        print(f"{numero1} - {numero2} = {total}")
    elif operador == "*":
        total = numero1 * numero2
        print(f"{numero1} * {numero2} = {total}")
    elif operador == "/":
        total = numero1 / numero2
        print(f"{numero1} / {numero2} = {total}")
    else:
        print("Operador Inválido")

calculadora()