from time import sleep
from random import choice

print('-=-'*14)
print('Tente adivinhar um número entre 0 e 5...')
print('-=-'*14)

numero = int(input('Digite o número: '))

numeroPc = choice([0, 1, 2, 3, 4, 5])

if numero == numeroPc:
	print(f'VOCÊ ACERTOU!! O número certo é {numeroPc}')
else: 
	print(f'\nVOCÊ ERROU!! O número certo era {numeroPc}') 
