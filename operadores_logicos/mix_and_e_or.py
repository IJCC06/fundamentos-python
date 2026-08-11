# Operadores "AND" e "OR"

def posso_entrar_no_show():
    POSSUI_INGRESSO = True
    idade = int(input("Digite sua idade: "))
    nome_esta_na_lista = bool(input("Seu nome está na lista? "))
    posso_entrar = idade >= 18 and (nome_esta_na_lista or POSSUI_INGRESSO)
    print(f"Vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_show()