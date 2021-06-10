#Tabuada 2.0
print("    ========= Tabuada 2.0 =========\n")
fator = int(input("> Digite um número para ver sua tabuada: "))
print("--"*22)

for fator2 in range(1, 11):
	produto = fator*fator2
	print(f"{fator} x {fator2} = {produto}")

print("--"*22)
