cont = soma = 0
while True:
	num = int(input(">> Digite um número(999 para parar): "))
	if num == 999:
		break
	soma = soma + num
	cont = cont +1
print(f">> O total de números digitados foi {cont}\n>> E a soma deles é {soma}")
