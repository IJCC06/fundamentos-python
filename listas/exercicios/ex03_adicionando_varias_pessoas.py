def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(f"Os novos convidados {novos_convidados} foram adicionados à lista de convidados")
    print(f"Nova lista de Convidados: {convidados}")

lista_de_nomes = ["Gabriel", "Lucas", "João", "Maria"]
novos_convidados = ["Mariana", "Cristiano", "Lionel"]

adicionar_convidados(lista_de_nomes, novos_convidados)