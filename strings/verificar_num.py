def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print("O valor digitado é uma idade válida")
    else:
        print("Digite somente números")


idade = input("Digite sua idade: ")
validar_idade(idade)