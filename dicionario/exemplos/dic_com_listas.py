def calcular_media(notas):
    return sum(notas) / len(notas)

def aluno_completo():
    aluno = {
        "nome": "Renan",
        "idade": 17,
        "curso": "Desenvolvimento de Sistemas",
        "notas": [8.5, 8.6, 9.3, 6.0],
        "endereco": {
            "cidade": "Piracicaba",
            "rua": "Das Amoreiras",
            "numero": 1234,
            "telefone": "(19) 99847-3687"
        },
    }

    aluno["media"] = calcular_media(aluno["notas"])
    print(f"Notas do aluno '{aluno["nome"]}': {aluno["notas"]}")
    print(f"Média do aluno '{aluno["nome"]}': {aluno["media"]}")

aluno_completo()