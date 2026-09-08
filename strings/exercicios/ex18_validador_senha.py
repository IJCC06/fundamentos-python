def validar_senha(senha):
    if len(senha) < 8:
        print("Senha Inválida. A senha precisa ter mais de 8 caracteres.")
    elif not senha.isalnum():
        print("Senha Inválida. A senha precisa de ao menos uma letra e um número.")
    elif senha.isspace():
        print("Senha Inválida. A senha não pode conter espaços")
    else:
        print("Senha válida.")

senha = input("Digite sua senha: ")
validar_senha(senha)