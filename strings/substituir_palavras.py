def trocar_cidade(texto):
    texto_trocado = texto.replace("São Paulo", "Piracicaba")

    return texto_trocado

cidade = f"Eu moro em {input("Digite sua cidade: ")}"
print(trocar_cidade(cidade))