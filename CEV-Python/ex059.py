from time import sleep

n1 = int(input(">> Digite um número: "))
n2 = int(input(">> Digite outro número: "))
op = 0

while op != 5:
	sleep(1)
	print("\n  [1] Somar\n  [2] Multiplicar\n  [3] Maior\n  [4] Novos Números\n  [5] Sair do programa\n")
	op = int(input(">> Opção: "))
	
	if op > 5 or op < 1:
		print(">> Opção Inválida! Tente novamente.")
	
	elif op == 1:
		print(f">> {n1} + {n2} = {n1+n2}")
	
	elif op == 2:
		print(f">> {n1} x {n2} = {n1*n2}")
	
	elif op == 3:
		if n1 > n2:
			print(f">> {n1} é o maior número.")
		else:
			print(f">> {n2} é o maior número.")
	
	elif op == 4:
		n1 = int(input(">> Digite um número: "))
		n2 = int(input(">> Digite outro número: "))
print("\nFinalizando...")
sleep(1.5)
print("Fim do programa.")	
