def exibir_aluno():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "curso": "Desenvolvimento de Sistemas"
    }
    print("Nome: ", aluno["nome"])
    print("Idade: ", aluno["idade"])
    print("Curso: ", aluno["curso"])
    print("Nota: ", aluno.get("nota"))

exibir_aluno()