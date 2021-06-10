from random import choice

print("==============================")
print("=        Par ou Ímpar        =")
print("==============================")
vitoria = 0
opUsuario = "x"
while True:
	numUsuario = int(input("\n> Valor: "))
	while opUsuario not in "PI":
		opUsuario = str(input("> Par ou ímpar[P/I]: ")).upper().strip()
		
	if opUsuario == "I":
		opMaquina = "P"
	else:
		opMaquina = "I"
	numMaquina = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	print("------------------------------")
	soma = numMaquina + numUsuario
	print(f"> Você jogou {numUsuario} e a maquina {numMaquina}, o total é {soma}!")
	if soma % 2 == 0:
		if opUsuario == "P":
			print("> Você ganhou! Vamos jogar novamente.")
			vitoria += 1
		elif opMaquina == "P":
			print("> Você Perdeu!")
			break
	else:
		if opUsuario == "I":
			print("> Você ganhou! Vamos jogar novamente.")
			vitoria += 1
		elif opMaquina == "I":
			print("> Você Perdeu!")
			break

print("==============================")
print(f"\n> Fim de jogo! Total de vitórias: {vitoria}")
