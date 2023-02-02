# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o preço do produto: R$ '))
desc = preco - (preco / 100 * 5) 
print('Preço do produto com 5% de desconto aplicado: R$ {:.2f}'.format(desc))