def login():
    dados = {
        "usuario": "IJCC0101",
        "senha": "123456789"
    }

    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == dados["usuario"] and senha == dados["senha"]:
        print("Acesso Permitido!")
    else:
        print("Usuário ou Senha incorretos!")

login()