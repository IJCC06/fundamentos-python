def limpar_texto(texto):
    # Remove espaços no inicio e final do texto
    texto_limpo = texto.strip()
    # Remove espaços da esquerda -- .lstrip()
    # Remove espaços da direita -- .rtrip()

    return texto_limpo

texto_1 = "      Aprender Python é legal!!!!    "

print(f"Texto antes: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")