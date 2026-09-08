def criar_nome_completo(partes):
    nome_completo = " ".join(partes)
    return nome_completo

partes_nome = ["Gabriel", "Menegon", "Cassano"]
print(f"O nome completo é {criar_nome_completo(partes_nome)}")