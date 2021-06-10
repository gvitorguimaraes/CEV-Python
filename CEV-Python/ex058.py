#Jogo Advinhação 2.0
from time import sleep
from random import randint

print("=-=-=-="*6)
print("=          Jogo da advinhação 2.0        =")
print("=-=-=-="*6)
usuario = int(input("=> Tente adivinhar o número de 1 a 10: "))
print("=-=-=-="*6)
sleep(0.5)

maquina = randint(1,10)
tentativas = 1

if usuario == maquina:
	print("\n=> Você acertou!!\n")
else:
	while usuario != maquina:
		
		sleep(0.5)
		tentativas += 1 
		if usuario < maquina:
			print("=> Você errou! Tente um número maior...")
		else:
			print("=> Você errou! Tente um número menor...")
		print("\n-------------------\n")
		usuario = int(input("=> Tente novamente: "))
	
	print("=> Você Acertou!\n")
	
print("=-=-=-="*6)
print(f"=> Número do computador: {maquina} ")
print(f"\n=> Suas tentativas.... {tentativas}")
print("\n=-=             Fim de jogo!           =-=")
