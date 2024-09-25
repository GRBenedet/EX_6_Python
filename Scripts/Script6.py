#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('digite seu nome completo: ')).title().strip()

separado = nome.split()

print('seu  primeiro nome é {} e seu ultimo nome é {}.'.format(separado[0] , separado[len(separado) - 1]))