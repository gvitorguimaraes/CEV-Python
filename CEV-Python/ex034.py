salario = float(input(' Digite o salário do funcionário: '))

if salario <= 1250:
	aumento = salario*1.15
	print(f' O salario desse funcionário passa a ser R${aumento:.2f} com o aumento de 15%.')
else:
	aumento = salario*1.1
	print(f' O salario desse funcionário passa a ser R${aumento:.2f} com o aumento de 10%.')
