palavra = "abc"
lista = []

for p in palavra:
    lista.append(p)

print(lista)

#ord - converte caractere em seu número de referência na tabela ASCII
print(ord("a"))

#chr - converte número inteiro para a grafia da linha da tabela ASCII
print(chr(97))

#Também é possível criar a lógica dentro da lista
lista2 = [p for p in palavra]
print(lista2)