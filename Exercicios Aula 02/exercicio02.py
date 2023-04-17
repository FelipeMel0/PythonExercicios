#Cada laranja custa R$0,30, mas quando comprada acima de uma dúzia, seu valor cai para R$0,25 cada
numeroLaranja = float(input("Quantas laranjas você quer comprar? "))

#Verificação de número de laranjas compradas
if numeroLaranja < 12:
    precoLaranja = 0.3
    valorFinal = numeroLaranja * precoLaranja
else:
    precoLaranja = 0.25
    valorFinal = numeroLaranja * precoLaranja

print(f"{numeroLaranja} laranjas por R${precoLaranja} totaliza R${valorFinal}")