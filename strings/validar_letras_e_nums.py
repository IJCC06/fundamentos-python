def validar_usuario(usuario):
    usuario_valido = usuario.isalnum()

    if usuario_valido:
        print("Usuário Verificado!")
    else:
        print("Usuário Inválido!")
        print("Utilize apenas letras e números")

usuario = input("Digite o nome de usuário: ")
validar_usuario(usuario)