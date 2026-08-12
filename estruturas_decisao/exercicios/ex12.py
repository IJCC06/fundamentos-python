def verificador():
    senha_correta = "python123"
    senha_input = input("Digite a senha: ")

    if senha_input == senha_correta:
        print("Acesso Permitido")
    else:
        print("Senha Inválida")

verificador()