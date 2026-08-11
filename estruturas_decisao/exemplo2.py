def login():
    e_mail = "juninmatadordeporco@gmail.com"
    senha = "1234"
    codigo_secreto = "#!#!#!"

    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if e_mail_input == e_mail and senha_input == senha:
        print("Usuário Logado!")
        acessar_admin = input("Deseja acessar a Área Adminstrativa?(S ou N) ")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite o código secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("Acesso ADM Liberado!")
            else:
                print("Código Incorreto!")
        elif acessar_admin == "N":
            print("OK. Acesso de Usuário!")
        else:
            print("Opção Inválida")
    else:
        print("E-mail ou senha incorretos!")

login()