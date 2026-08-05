def comissao():
    salario_fixo = float(input("Digite seu salário fixo: "))
    valor_vendas = float(input("Digite o valor das vendas: "))
    percentual_comissao = float(input("Digite a taxa de comissão: ")) / 100
    salario_final = salario_fixo + (valor_vendas * percentual_comissao)
    print(f"O salário final é de R$ {salario_final}")

comissao()