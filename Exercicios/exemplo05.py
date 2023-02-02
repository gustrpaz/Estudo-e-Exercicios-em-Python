# Operadores Aritiméticos

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão inteira
# % Resto da divisão

#  ,end= ' ' Para não quebrar a linha

conta1 = 5 + 3 * 2 
conta2 = 3 * 5 + 4 ** 2
conta3 = 3*(5+4)**2

print('{},{},{} \n'.format(conta1,conta2,conta3))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' Soma é {} \n Subtração é {} \n Produto é {} \n Divisão é {:.3f}'.format(s,su,m,d))
print(' Divisão inteira {} \n Potência é {}'.format(di,e))