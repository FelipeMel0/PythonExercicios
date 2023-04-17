# Fazer um programa em que o usuário entra com o ano de seu nascimento e o programa imprime na tela ssua idade.

# ano = int(input("Em que ano você nasceu?"))
# idade = 2023 - ano
# print(f"Você tem {idade} anos")

# Exemplo usando a biblioteca Datetime
import datetime
# Declaração da variável
year = int(input("Em que ano você nasceu? "))
actualYear = datetime.datetime.now()
actualYear = (actualYear.year)
# Calcular aniversário
age = actualYear - year
nextAge = age + 1
# Imprimir na tela o aniversário
print(
    f"Você nasceu no ano de {year} e, atualmente, em {actualYear}, você tem {age} anos. Ano que vem você terá {nextAge} anos!")
