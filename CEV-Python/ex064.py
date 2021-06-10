total = n = c = 0
n = int(input(">> Digite um número [999 para finalizar]: "))
while n != 999:
	total += n
	c += 1
	n = int(input(">> Digite um número [999 para finalizar]: "))
print(f">> A soma de todos os {c} valores digitados é: {total}")
