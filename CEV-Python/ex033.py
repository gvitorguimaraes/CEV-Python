numA = int(input('> Digite um numero: '))
numB = int(input('> Digite outro numero: '))
numC = int(input('> Digite mais um numero: '))

print('-=-'*10)
if numA > numB and numA > numC:
	print(f'> O maior número é {numA}')
elif numB > numA and numB > numC:
	print(f'> O maior número é {numB}')
elif numC > numA and numC > numB:
	print(f'> O maior número é {numC}')
print('\n')
if	numA < numB and numA < numC:
	print(f'> O menor número é {numA}')
elif numB < numA and numB < numC:
	print(f'> O menor número é {numB}')
elif numC < numA and numC < numB:
	print(f'> O menor número é {numC}')
print('-=-'*10)
