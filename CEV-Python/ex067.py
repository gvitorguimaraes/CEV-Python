while True:
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	num = int(input(">> Digite um número para ver sua tabuada: "))
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	if num < 1:
		break
	for c in range(1, 11):
		print(f"{num} x {c} = {num*c}")
print("\n>> Fim do programa...!")
