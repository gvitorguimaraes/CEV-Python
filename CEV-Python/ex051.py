#Ler os termos de uma PA
print("=="*17)
print("=      Progressão Aritimética    =")
print("=="*17)

termoInicial = int(input("> Digite o primeiro termo: "))  
razao = int(input("> Digite a razão da progressão: "))

print("=="*17)

for p_a in range(1, 11):
	print(f"=> {termoInicial}")
	termoInicial += razao
	
print("=="*17)
