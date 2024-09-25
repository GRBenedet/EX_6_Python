#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Digite seu nome completo: ')).strip()


print('SILVA' in name.upper())


print('Silva' in name.title())