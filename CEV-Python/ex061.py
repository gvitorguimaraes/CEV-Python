print("============ PA ============")
x = int(input(">> Digite primeiro termo: "))
r = int(input(">> Digite a razão: "))
pa = x
i = 1
print("============================\n")
while i <= 10:
	print(f" {pa} → " ,end='')
	pa += r
	i += 1
print("FIM")
