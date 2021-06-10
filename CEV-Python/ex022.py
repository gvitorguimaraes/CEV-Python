from time import sleep

nome = input('Digite seu nome completo: ').strip()
print('\n  .... Analisando seu nome ....\n')
sleep(0.5)
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
nomeSep = nome.split()
print('Seu nome ao todo tem {} letras.'.format(len(''.join(nomeSep))))
print(f'Seu primeiro nome é {nomeSep[0]}')
print(f'Seu primeiro e segundo nome é {nomeSep[0]} {nomeSep[1]}')
