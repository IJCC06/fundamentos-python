def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    compras.remove(produto)


compras = ["Arroz", "Feijão", "Leite"]

novos_produtos = ["Pão", "Café", "Açúcar"]

adicionar_produtos(compras, novos_produtos)

print(compras)

cancelar_compra(compras, "Leite")

print(compras)