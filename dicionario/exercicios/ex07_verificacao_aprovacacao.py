def verificar_aprovacao():
    dados = {
        "nome": "Gabriel",
        "nota": 8.5,
        "frequencia": 88
    }

    if dados["nota"] >= 6 and dados["frequencia"] >= 75:
        print(f"O aluno {dados["nome"]} foi aprovado!")
    else:
        print(f"O aluno {dados["nome"]} foi reprovado!")

verificar_aprovacao()