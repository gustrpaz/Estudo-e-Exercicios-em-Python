# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = int(input('Informe o valor em metros para a conversão: '))
cent= n * 100
mili= n * 1000
print('Centímetros = {} cm\nMilímetros = {} mm'.format(cent,mili))