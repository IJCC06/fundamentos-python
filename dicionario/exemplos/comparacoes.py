def verificar_aprovacao():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "nota": 8.5,
        "frequencia": 88
    }

    if aluno["nota"] >= 6 and aluno["frequencia"] >= 75:
        print(f"O aluno {aluno["nome"]} foi aprovado!")
    else:
        print(f"O aluno {aluno["nome"]} foi reprovado!")

verificar_aprovacao()