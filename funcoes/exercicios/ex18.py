def prestacao():
    valor_do_produto = float(input("Digite o valor do produto: "))
    quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
    parcelas = valor_do_produto // quantidade_parcelas
    print(f"O valor da parcela será de R$ {parcelas}")

prestacao()