from time import sleep
velocidade = float(input('> Informe a velocidade do veículo: '))

if velocidade > 80:
	multa = (velocidade-80)*7
	print(f'> MULTADO! Você ultrapassou o limite de velocidade permitido na via.\n> Deverá pagar uma multa de R${multa:.2f}')

else:
	print('Tenha um bom dia! Dirija com segurança.')
sleep(10)