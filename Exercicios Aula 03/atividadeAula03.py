metaVendas = 50000
quantidadeVendas = float(input("Digite quantas unidades do produto foram vendidas (utilize '.' para casas decimais): "))
salarioVendedores = 1362

if quantidadeVendas < metaVendas:
    print('A meta não foi atingida. Ninguém recebe bônus. O salário continua R${}'.format(salarioVendedores))
elif (quantidadeVendas - metaVendas) < 500:
    print('A meta foi atingida. Os vendedores ganharão 5% de bônus, portando o salário será de R${:.2f}'.format(salarioVendedores * 1.05))
else:
    print('A meta foi atingida. Os vendedores ganharão 15% de bônus, portando o salário será de R${:.2f}'.format(salarioVendedores * 1.15))