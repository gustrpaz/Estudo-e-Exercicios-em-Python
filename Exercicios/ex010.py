# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

valor =  float(input('Informe o valor em reais da quantia presente na carteira: '))
conta = (valor / 3.27) 
print ('Você poderá obter US$ {:.2f} '.format(conta))