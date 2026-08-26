def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente


fila = []

while True:
    cliente = input("Digite o nome do cliente (ou 'sair' para terminar): ")

    if cliente.lower() == "sair":
        break

    adicionar_cliente(fila, cliente)

print("\nFila de atendimento:", fila)

if len(fila) > 0:
    print("Cliente atendido:", atender_cliente(fila))
    print("Fila atualizada:", fila)