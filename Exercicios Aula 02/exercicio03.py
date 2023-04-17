# Declaração dos segmentos
try:
    seg1 = float(input("Digite o tamanho do primeiro segmento: "))
    seg2 = float(input("Digite o tamanho do segundo segmento: "))
    seg3 = float(input("Digite o tamanho do terceiro segmento: "))
except ValueError:
    print("Valor inválido! Digite apenas números.")
    exit()

if seg1 <= 0 or seg2 <= 0 or seg3 <= 0:
    print("Dados inválidos. Os números são negativos ou iguais a zero.")
else:
    if seg1 > seg2 and seg1 > seg3:
        somaMenorSeguimentos = seg2 + seg3
        if somaMenorSeguimentos > seg1:
            print("Esses segmentos formam um triângulo")
        else:
            print("Esses segmentos NÃO formam um triângulo")
    elif seg2 > seg1 and seg2 > seg3:
        somaMenorSeguimentos = seg1 + seg3
        if somaMenorSeguimentos > seg2:
            print("Esses segmentos formam um triângulo")
        else:
            print("Esses segmentos NÃO formam um triângulo")
    elif seg3 > seg1 and seg3 > seg2:
        somaMenorSeguimentos = seg2 + seg1
        if somaMenorSeguimentos > seg3:
            print("Esses segmentos formam um triângulo")
        else:
            print("Esses segmentos NÃO formam um triângulo")
    else:
        print("Todos os segmentos são iguais e formam um triângulo")
    
