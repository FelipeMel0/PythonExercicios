lista = []
contador = 0

quantidadePar = 0
quantidadeImpar = 0

while contador <= 10:
        lista.append(contador)

        if contador % 2 == 0:
            quantidadePar += 1
        else:
            quantidadeImpar += 1
        contador += 1

print(lista)
print(f'Par: {quantidadePar}')
print(f'Ímpar: {quantidadeImpar}')
