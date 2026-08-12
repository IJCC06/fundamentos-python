def idade():
    idade = int(input("Digite sua idade: "))

    if idade > 0 and idade < 18:
        print("Menor de Idade")
    elif idade >= 18:
        print("Maior de idade")
    else:
        print("Digite uma idade certa, seu imbecil")

idade()