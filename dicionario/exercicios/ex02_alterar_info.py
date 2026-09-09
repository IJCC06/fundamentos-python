def alterar_informacoes():
    aluno = {
        "nome": "Gabriel",
        "idade": 16,
        "telefone": "(19) 94536-0909",
        "endereco": "Rua das Flores, 123",
        "cidade": "Piracicaba",
        "nota": [10, 8.9, 9, 7.8],
        "turma": "1",
        "curso": "Desenvolvimento de Sistemas"
    }

    print("Antes:")
    print(f"Idade: {aluno["idade"]}")
    print(f"Cidade: {aluno["cidade"]}\n")

    aluno["idade"] = int(input("Digite a nova idade: "))
    aluno["cidade"] = input("Digite a nova cidade: ")

    print("\nDepois:")
    print(f"Idade: {aluno["idade"]}")
    print(f"Cidade: {aluno["cidade"]}")

alterar_informacoes()