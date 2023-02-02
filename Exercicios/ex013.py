# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o salário atual do funcionário: R$ '))
aumento = (salario / 100) * 15
final = salario + aumento
print('Novo salário com 15% de aumento: R$ {:.2f}'.format(final))
