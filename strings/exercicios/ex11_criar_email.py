def criar_email(nome, sobrenome, dominio):
    email = nome.lower() + "." + sobrenome.lower() + "@" + dominio.lower()

    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Domínio: {dominio}")
    print(f"\nSaída: {email}")

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
dominio = input("Digite seu domínio: ")
criar_email(nome, sobrenome, dominio)