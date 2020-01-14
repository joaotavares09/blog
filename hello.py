# -*- coding: UTF-8 -*-
print('Hello, Django boys!')
if 3 > 2:
    print('3 é maior que 2')
else:
    print('não é maior que 2')
name = 'Sonja'
if name == 'Olá':
    print('Ola Ola!')
elif name =='Sonja':
    print('Olá Sonja\n')
else:
    print('Olá Estranho!')

def oi(nome):
    print('Oi '+nome+'!')

girls = ['Raquel', 'Monica', 'Phoebe', 'Olá', 'voçê']

for name in girls[::2]:
    oi(name)
    print('Próxima!\n')
