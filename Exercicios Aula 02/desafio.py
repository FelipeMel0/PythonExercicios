tipoConbustivel = input("Digite o tipo de combustível que deseja (A - Álcool / G - Gasolina):").casefold()
quantidadeLitro = float(input("Digite quantos litros você deseja colocar: "))
precoGasolina = 5
precoAlcool = 4

if tipoConbustivel == "a":
    if quantidadeLitro < 20 or quantidadeLitro == 20:
        valorFinal = quantidadeLitro * precoAlcool - (quantidadeLitro * precoAlcool)  * 0.03
        print(f'O valor total é de R${valorFinal}')
    else:
        valorFinal = quantidadeLitro * precoAlcool - (quantidadeLitro * precoAlcool)  * 0.05
        print(f'O valor total é de R${valorFinal}')
elif tipoConbustivel == "g":
    if quantidadeLitro < 20 or quantidadeLitro == 20:
        valorFinal = quantidadeLitro * precoGasolina - (quantidadeLitro * precoGasolina)  * 0.04
        print(f'O valor total é de R${valorFinal}')
    else:
        valorFinal = quantidadeLitro * precoGasolina - (quantidadeLitro * precoGasolina)  * 0.06
        print(f'O valor total é de R${valorFinal}')
else:
    print("Opção inválida")
    exit()