print("============================")
print("=  Sequência de Fibonacci  =")
print("============================\n")

n = int(input(">> Digite o número de termos: "))
i = 3
n1 = 0
n2 = 1

print(f"\n {n1} → {n2} → ", end="")
while i <= n:
	n3 = n1 + n2
	print(f"{n3} → ", end="")
	n1 = n2
	n2 = n3
	i += 1
print("FIM")
