def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(f"O aluno {nome} foi adicionado na posição {posicao}")
    print(f"Lista de Alunos Atualizada: {alunos}")

lista_de_nomes = ["Gabriel", "Lucas", "João", "Maria"]
novo_aluno = input("Digite o nome do novo aluno: ")
posicao = int(input("Qual a posição desse aluno? "))

inserir_aluno(lista_de_nomes, novo_aluno, posicao)