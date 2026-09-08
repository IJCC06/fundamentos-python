def validar_especie(animal):
    animal_validado = animal.isalpha()

    print(f"Entrada: {animal}")
    if animal_validado:
        print("Espécie de animal válida.")
    else:
        print("Espécie inválida.")

animal = input("Digite a espécie de animal: ")
validar_especie(animal)