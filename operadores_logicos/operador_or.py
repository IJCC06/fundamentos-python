# Operador "OR"
def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("Você tem dinheiro? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Vou comer um Mc Donald's hoje? {autorizado}")

posso_comprar()