def exibir_mensagem():
    print("Hello World!!!!")

def somar(valor1,valor2):
    total = valor1 + valor2
    print(total)

def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    return media

exibir_mensagem()
somar(23, 45)

nota = calcular_media()
print(nota)