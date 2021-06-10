from time import sleep

valorCasa = float(input('> Digite o valor da casa: '))
salario = float(input('> Digite o seu salário: R$'))
anos = int(input('> Em quantos anos deseja pagar: '))

parcelas = valorCasa/(anos*12)

sleep(0.5)
if parcelas < (salario*0.3):
    print('\n#==== O seu empréstimo foi APROVADO! ====#')
    print(f'\n> Você pagará parcelas de R${parcelas:.2f}')
else:
    print('\n#==== O seu empréstimo foi NEGADO! ====#')
