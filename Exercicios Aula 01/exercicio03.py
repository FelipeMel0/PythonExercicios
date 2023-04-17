#Fazer um programa em qeue o usuário entra com um número e o programa imprime na tela seu antecessor e seu sucessor.

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print(f"Antecessor de {numero} = {antecessor}") #f é a abreviação de "format"
print("Sucessor de {} = {}".format(numero, sucessor))