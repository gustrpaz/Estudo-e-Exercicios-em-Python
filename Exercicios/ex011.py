# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Informe em metros a dimensão da parede: \nLargura: '))
altura = float(input('Altura: '))
area = largura * altura
qtde = area / 2

print('\nInformações: \nA área dessa parede é de: {:.3f}m² \nQuantidade de tinta para pintar essa parede: {:.3f}L\n'.format(area,qtde))