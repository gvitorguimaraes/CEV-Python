#Ler o peso e indicar o maior e menor
maior = 0
menor = 0

for entrada in range(0, 5):
	pesos = float(input(f"> {entrada+1}° peso: "))
	if entrada == 1:
		maior = pesos
		menor = pesos
	else:
		if pesos > maior:
			maior = pesos
		if pesos < menor:
			menor = pesos
print(f"\n> Maior peso {maior}Kg")
print(f"> Menor peso {menor}Kg")
