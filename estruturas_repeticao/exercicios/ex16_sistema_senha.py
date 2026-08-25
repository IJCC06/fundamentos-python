def validar_senha(senha_correta):
    tentativa = 0

    while tentativa < 3:
        senha = int(input("Digite a senha: "))

        if senha == senha_correta:
            print("Acesso Autorizado!")
            return 0
        else:
            print("Acesso Negado")
            tentativa += 1

    print("Tentativas Expiradas")


validar_senha(1234)