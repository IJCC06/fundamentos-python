import time

def contagem_regressiva():
    valor_contagem = int(input("Digite um número maior que 0: "))
    if valor_contagem < 0:
        print("O valor é inválido! Seu Burro")
    else:
        print("Contagem Regressiva:")
        while valor_contagem > 0:
            print(valor_contagem)
            valor_contagem -= 1
            time.sleep(1)
        print("DECOLAGEM AUTORIZADA")

contagem_regressiva()