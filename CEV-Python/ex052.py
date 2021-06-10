#Verificar se um numero é primo
print("==================================")
print("==        Numeros primos        ==")
print("==================================")

numero = int(input("=> Numero: "))
div = 0

for primo in range(2, numero):  # Laço com range entre 2 e o numero anterior ao numero digitado;
	test = numero % primo		# Testa se o resto da divisão entre o numero digitado e a sequencia do laço é 0;
	if test == 0:			# Se for, então esse número nao pode ser primo;
		div = 1			# A variável div recebe o valor 1;

print("\n----------------------------------\n")

if div == 0:			# Se o valor de div for 0 significa que ele não foi divisivel pro nenhum numero do laço, portanto é um numero primo;
	print(f"=> O número {numero} é PRIMO!")
else:
	print(f"=> O número {numero} NÃO é primo!")	
