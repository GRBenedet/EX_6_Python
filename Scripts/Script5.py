#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('digite uma frase aleatoria: ')).lower().strip()

print('A letra "a" aparece {} vezes.\nA primeira letra "a" aparece na posição {}.\n a ultima vezes que a a letra "a" aparece é na posição {}.'.format(frase.count('a') , frase.find('a') + 1 , frase.rfind('a') + 1))