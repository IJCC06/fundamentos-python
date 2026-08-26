def remover_item(itens, posicao):
    item_removido = itens.pop(posicao)
    return item_removido


itens = ["Maçã", "Banana", "Laranja", "Uva"]

print(remover_item(itens, 1))
print(itens)