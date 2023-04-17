vendas = [1070, 150, 1500, 2000, 120]
vendedores_com_bonus = []

for indice, venda in enumerate(vendas):
    if venda > 1000:
        vendedores_com_bonus.append(indice)

print("Os vendedores que conseguiram o bônus são:", vendedores_com_bonus)

# vendas = [19900, 150, 1500, 2000, 120]

# for i in range(len(vendas)):
#     if vendas[i] > 1000:
#         print("O vendedor na posição", i, "conseguiu o bônus!")