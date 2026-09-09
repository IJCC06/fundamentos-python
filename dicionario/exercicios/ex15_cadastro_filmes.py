def cadastrar_filmes():
    dados = {
        "titulo": "Indiana Jones e a Lenda do Amanhã",
        "ano": 2024,
        "genero": "Aventura",
        "notas": []
    }

    for nota in range(5):
        dados["notas"].append(float(input(f"Digite a avaliação {nota + 1}: ")))

    dados["media"] = sum(dados["notas"]) / len(dados["notas"])
    print(f"Média de Avaliação do Filme: {dados["media"]:.2f}")

cadastrar_filmes()