def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")

lista_de_nomes = ["Gabriel", "João", "Lula", "Vorcaro"]
juntar_nomes(lista_de_nomes, ["Rafael", "Vínicius"])