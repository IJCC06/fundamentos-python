def autenticacao():
    usuario = "admin"
    senha = "1234"
    usuario_input = input("Digite o usuário: ")
    senha_input = input("Digite a senha: ")

    if usuario_input != usuario and senha_input != senha:
        print("Usuário e Senha incorretos")
    elif usuario_input == usuario and senha_input == senha:
        print("Login realizado com sucesso")
    elif usuario_input == usuario and senha_input != senha:
        print("Senha Incorreta")
    elif usuario_input != usuario and senha_input == senha:
        print("Usuário Incorreto")

autenticacao()