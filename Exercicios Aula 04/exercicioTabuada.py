numero = int(input("Digite um número: "))
contador = 1
print("Tabuada do {}".format(numero))

while contador <= 10:
    print("{} x {} = {}".format(numero, contador, numero * contador))
    contador += 1