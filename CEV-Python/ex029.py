print('---------------------------------')
velocidade = float(input(' Digite a velocidade do carro: '))
print('---------------------------------\n')
if velocidade > 80:
	multa = (velocidade - 80)*7
	print(f' MULTADO! Você está acima do limite de velocidade.\n Deverá pagar uma multa de R${multa}')
else:
	print(' Você está dentro do limite de velocidade!')
print(' Tenha um bom dia! Dirija com segurança.')
