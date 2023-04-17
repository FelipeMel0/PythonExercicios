#Declaração das variáveis
primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

#Verificação do maior número
if primeiroNumero > segundoNumero:
    print(f'O maior número é: {primeiroNumero}')
elif primeiroNumero == segundoNumero:
    print("Os dois números são iguais")
else:
    print(f'O maior número é: {segundoNumero}')