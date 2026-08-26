def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)


pontuacoes = [150, 300, 100, 500, 250]

print(criar_ranking(pontuacoes))