def adicionar_informacoes():
    aluno = {
            "nome": "Carlos",
            "idade": 18,
    }
    print("Aluno Antes: ", aluno)
    aluno["curso"] = "Técnico em Eletrônica"
    aluno["nota"] = 9.8
    print("Aluno Depois: ", aluno)

adicionar_informacoes()