from time import sleep
nome = input('Digite um nome: ').title().strip().split()
print('Muito prazer em conhecê-lo!')
sleep(0.5)
print(f'O seu primeiro nome é {nome[0]}')
print(f'O seu ultimo nome é {nome[-1]}')
