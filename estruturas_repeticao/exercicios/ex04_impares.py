def mostrar_impares(numero):
    contador = 1
    while contador <= numero:
        if (contador % 2) != 0:
            print(contador)
        contador += 1

mostrar_impares(20)