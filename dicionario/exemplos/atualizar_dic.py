def atualizar_idade():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "curso": "Desenvolvimento de Sistemas"
    }

    print("Idade antes: ", aluno.get("idade"))
    aluno["idade"] = 20
    print("Idade Depois: ", aluno.get("idade"))

atualizar_idade()