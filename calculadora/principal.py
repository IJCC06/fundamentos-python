from calculadora import *

def executar_calculadora():
    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print("\n======CALCULADORA======")
        print("***** ESCOLHA UMA OPERAÇÃO: *****")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "0":
            print("--- CALCULADORA ENCERRADA! ---")
            break

        if opcao not in operacoes:
            print("OPÇÃO INVÁLIDA")
            continue

        numero_a = float(input("Digite o primeiro número: "))
        numero_b = float(input("Digite o segundo número: "))

        funcao = operacoes[opcao]
        resultado = funcao(numero_a, numero_b)
        print(f"O resultado da operação é {resultado}")

executar_calculadora()