def aluno_aprovado():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    media = (nota_1 + nota_2) / 2

    print(f"Sua média foi {media}")

    if media >= 6:
        print("Aluno Aprovado!")
    elif media >= 5 and media < 6:
        print("Aluno de Recuperação")
    else:
        print("Aluno Reprovado")

aluno_aprovado()