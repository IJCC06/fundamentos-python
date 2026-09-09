def analise_notas():
    dados = {
        "nome": "Carlos",
        "notas": [9.1, 8.6, 10]
    }

    maior_nota = max(dados["notas"])
    menor_nota = min(dados["notas"])
    media = sum(dados["notas"]) / len(dados["notas"])

    print("Relatório de Desempenho:")
    print(f"Nome: {dados["nome"]}")
    print(f"Notas: {dados["notas"]}")
    print(f"Maior Nota: {maior_nota}")
    print(f"Menor Nota: {menor_nota}")
    print(f"Média: {media:.2f}")

analise_notas()