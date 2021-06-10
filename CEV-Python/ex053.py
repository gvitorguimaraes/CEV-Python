#Verificar se uma frase é um palindromo
frase = input("Digite uma frase: ").strip().upper()
sep =  frase.split()
junto = "".join(sep)
inv = junto[::-1]

if junto == inv:
	print("> A frase digitada é um palíndromo.")
	print(junto, inv)
else:
	print("> A frase digitada não é um palíndromo.")
	print(junto, inv)
