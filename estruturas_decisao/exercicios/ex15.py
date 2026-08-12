def radar():
    velocidade = int(input("Digite a velocidade do veículo: "))

    if velocidade <= 60:
        print("Velocidade Permitida")
    elif 61 <= velocidade <= 80:
        print("Atenção: Velocidade Acima do Permitido")
    elif velocidade > 80:
        print("Multa por Excesso de Velocidade")
    else:
        print("Leitura Inválida")

radar()