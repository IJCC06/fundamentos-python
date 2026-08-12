def classificacao_triangulo():
    lado1 = round(float(input("Digite o primeiro lado: ")), 1)
    lado2 = round(float(input("Digite o segundo lado: ")), 1)
    lado3 = round(float(input("Digite o terceiro lado: ")), 1)

    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Triângulo Isósceles")
    elif lado1 != lado2 != lado3:
        print("Triângulo Escaleno")

classificacao_triangulo()