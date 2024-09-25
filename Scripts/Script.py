#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# – O nome com todas as letras maiúsculas e minúsculas. 
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.


name = input('digite seu nome completo: ')

print('O nome com todas as letras em maiusculas: {}'.format(name.upper()))
print('O nome com todas as letras minusculas: {}'.format(name.lower()))
print('o total de letras nesse nome é {}.'.format(len(name) - name.count(' ')))
print('O primeiro nome tem {} letras.'.format(name.find(' ')))