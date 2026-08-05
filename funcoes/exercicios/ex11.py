def salario():
    valor_hora = float(input("Digite o valor da sua hora: "))
    horas = int(input("Digite as horas trablhadas: "))
    salario = valor_hora * horas
    print(f"Você trabalhou {horas} horas por R$ {valor_hora}/hora.")
    print(f"Seu salário é de R$ {salario}")

salario()