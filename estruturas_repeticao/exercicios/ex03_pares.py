def mostrar_pares(numero):
    contador = 1
    while contador <= numero:
        if (contador % 2) == 0:
            print(contador)
        contador += 1

mostrar_pares(20)