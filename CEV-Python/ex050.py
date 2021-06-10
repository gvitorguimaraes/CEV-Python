#Ler 6 inteiros e somar se for par
soma = 0
for inteiro in range(1,7):
	num = int(input("> Digite um inteiro: "))
	if num % 2 == 0:
		soma = soma+num
print(f"\n> A soma dos numeros pares digitados é: {soma}")
