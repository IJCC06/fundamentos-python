def desconto():
    preco_produto = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o percentual de desconto: ")) / 100
    valor_final = preco_produto * (1 - desconto)
    print(f"O valor final é R$ {valor_final}")

desconto()