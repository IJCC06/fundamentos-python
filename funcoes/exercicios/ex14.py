def consumo_combustivel():
    distancia = float(input("Digite a distância percorrida (em km): "))
    combustivel_consumido = float(input("Digite a quantidade de combustivel consumidos (em L): "))
    consumo_medio =  distancia / combustivel_consumido
    print(f"O consumo médio foi de {consumo_medio} Km/L")

consumo_combustivel()