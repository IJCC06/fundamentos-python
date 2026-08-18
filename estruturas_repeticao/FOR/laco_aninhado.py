def laco_aninhado():
    nomes = ["Renan", "Moises", "Rafael"]
    notas = [8, 9, 10]

    for nome in nomes:
        print(f"Nome do Aluno: {nome}")
        for nota in notas:
            print(f"Nota do Aluno: {nota}")

laco_aninhado()