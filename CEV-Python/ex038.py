print('#===================================#')
num1 = int(input('> Digite um número inteiro: '))
num2 = int(input('> Digite outro número inteiro: '))
print('#===================================#')

if num1 != num2:
	if num1 > num2:
		print(f'> O maior número digitado foi: {num1}')
	else:
		print(f'> O maior número digitado foi: {num2}')
else:
	print('> Os dois números são iguais!')