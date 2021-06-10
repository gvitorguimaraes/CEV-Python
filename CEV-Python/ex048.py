#Soma impares multiplos de 3 entre 1 - 500
print("=== Soma dos multiplos de 3 entre 1 e 500 ===")
soma = 0
count = 0
for impar in range(1,501, 2):
	if (impar % 3) == 0:
		count += 1
		soma += impar
print(f"\nTotal de elementos somados: {count}")
print(f"\nO resultado da soma: {soma}")
