def verificar_chave():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
    }

    if "nome" in aluno:
        print("O nome está cadastrado!")

    if "nota" not in aluno:
        print("A nota não está cadastrada!")

verificar_chave()