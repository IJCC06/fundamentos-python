def verificar_extensao(nome_arquivo):
    arquivo_validado = nome_arquivo.endswith(".pdf")

    print(f"Entrada: {nome_arquivo}")
    if arquivo_validado: print("Arquivo válido.")
    else: print("Arquivo inválido.")

arquivo = input("Digite o nome do arquivo e sua extensão: ")
verificar_extensao(arquivo)