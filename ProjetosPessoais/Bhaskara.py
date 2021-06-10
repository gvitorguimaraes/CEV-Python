from math import sqrt
from time import sleep

while (True):
	print('-----------------------------\n')
		
	a = int(input('-> Digite o valor de A: '))
	b = int(input('-> Digite o valor de B: '))
	c = int(input('-> Digite o valor de C: '))

	sleep(0.5)

	if b == 0:
		if c > 0:
			print('-> Essa equação não possui raizes reais!')
		
		else:
			rest1 = sqrt((c*-1)/a)
			print(f'-> As raizes dessa equação são -{rest1} e +{rest1}.')

	elif c == 0:
			rest2 = -b/a
			print(f'-> As raizes dessa equação são 0 e {rest2}.')
			print(delta)
	
	elif c == 0 and b == 0:
		print('-> As raiz dessa equação é 0.')

	else:
		delta = ((b**2)-4*a*c)
		if delta >= 0:
			resultado1 = (-(b) + (delta)**(1/2))/(2*a)
			resultado2 = (-(b) - (delta)**(1/2))/(2*a)
			print(f'\n-> As raizes dessa equação são {resultado1} e {resultado2}.')
		else:
			print('-> Essa equação não possui raizes reais.')
	print('\n-----------------------------')
	
