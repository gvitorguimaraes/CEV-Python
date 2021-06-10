#Ler o ano de nascimento e indica se já é de maior ou não
maior = 0
for c in range(0,7):
	ano = int(input("> Digite o ano de nascimento: "))
	if (2020-ano) >= 21:
		maior = maior + 1
print(f"> Maiores de 21 anos: {maior}")
print(f"> Menores de 21 anos: {7-maior}")
