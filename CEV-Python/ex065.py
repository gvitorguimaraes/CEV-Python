opcao = "S"
maior = menor = soma = c = 0

while opcao == "S":
	n = int(input(">> Digite um número: "))
	if c == 0:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		else:
			menor = n
	opcao = (input("Deseja continuar [S/N]? ")).strip().upper()
	soma += n
	c += 1
media = soma/c
print(f"\n>> Você digitou {c} números\n>> A média deles é {media}\n>> O maior valor é {maior} e o menor {menor}.")
