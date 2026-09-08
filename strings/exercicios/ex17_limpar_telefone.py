def limpar_telefone(numero):
    numero_limpo = numero.replace("(", "").replace(")", "").replace(" ", "")

    print(f"Saída: {numero_limpo}")

telefone = input("Digite seu número de telefone: ")
limpar_telefone(telefone)