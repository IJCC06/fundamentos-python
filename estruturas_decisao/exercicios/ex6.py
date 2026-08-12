def qual_e_o_maior():
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    if numero_1 > numero_2:
        print(f"O número {numero_1} é maior que o número {numero_2}")
    elif numero_1 < numero_2:
        print(f"O número {numero_2} é maior que o número {numero_1}")
    else:
        print("Os números são iguais!")

qual_e_o_maior()