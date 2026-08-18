# Laço "For" Simples
import time

def mostrar_numero():
    for i in range(1, 6):
        print(f"O número atual é {i}")
        time.sleep(1)

mostrar_numero()