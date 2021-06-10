print('===============================')
numero = int(input('> Digite um número inteiro: '))
print('===============================')
print(' => [1] Binário')
print(' => [2] Octal')
print(' => [3] Hexadecimal')
print('===============================')
opcao = int(input('> Opção: '))

if opcao == 1:
    print(f'> O número {numero} convertido para Binário é: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'> O número {numero} convertido para Octal é: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'> O número {numero} convertido para Hexadecimal é: {hex(numero)[2:]}')
else:
	print('\n> A opção digitada é inválida!')