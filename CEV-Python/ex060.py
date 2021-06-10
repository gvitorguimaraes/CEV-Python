print("========= Fatorial =========\n")
fat = int(input(">> Digite o número: "))

contador = fat - 1
out = f">> {fat} x {contador}"

while contador > 1:
	fat = fat * contador
	contador = contador - 1
	out = out+f" x {contador}"

print("")
print(out+f" = {fat}")
