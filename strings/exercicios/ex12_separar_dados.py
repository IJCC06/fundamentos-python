def separar_dados(dados):
    lista_de_dados = dados.split(", ")

    print(f'''
        Nome: {lista_de_dados[0]}
        Idade: {lista_de_dados[1]}
        Profissão: {lista_de_dados[2]}
        Cidade: {lista_de_dados[3]}
    ''')

dados = "João, 40, Desenvolvedor, Piracicaba"
separar_dados(dados)

