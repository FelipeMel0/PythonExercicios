#Criando variáveis
altura = float(input('Digite a sua altura em metros (use "." para casas decimais): '))
peso = float(input('Digite o seu peso em quilos (use "." para casas decimais): '))
sexo = input('Digite o seu sexo biológico (M para masculino / F para feminino): ').casefold()

#Verificando sexo biológico
if sexo == "M":
    pesoIdeal = (72.7 * altura) - 50
elif sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Opção inválida")
    exit()

#verificando peso
if peso > pesoIdeal:
    print('Você está acima do peso. O peso ideal seria de {:.2f}kg e você está com {}kg. Você precisa emagrecer {:.2f}kg. Lembre-se: Você é o projeto mais importante em que deve trabalhar.'.format(pesoIdeal, peso, peso - pesoIdeal))
elif peso == pesoIdeal:
    print(f'Você está no peso ideal! Atualmente, você está com {peso}kg. Parabéns!')
else:
    print('Você está abaixo do peso. O peso ideal seria de {:.2f}kg e você está com {}kg. Você precisa ganhar {:.2f}kg. Atente-se a isso!'.format(pesoIdeal, peso, pesoIdeal - peso))
