#Pedra papel tesoura
import random
from time import sleep

print("====== Jokenpô ======\n")
print("=> [1] Pedra")
print("=> [2] Papel")
print("=> [3] Tesoura")
print("\n=====================\n")

opcao = int(input("> Digite sua opção: "))
lista = ['pedra','papel',' tesoura']
opcaoComp = random.choice(lista) 

print("\n=====================\n")
sleep(0.30)
print(" JO ")
sleep(0.30)
print(" KEN ")
sleep(0.30)
print(" PÔ!!! \n")
sleep(0.75)
print("=====================\n")

if opcao == 1:
	if opcaoComp == "pedra":
		print("> Ambos jogaram pedra!")
		print("> EMPATE") 
	elif opcaoComp == "papel":
		print("> O computador escolheu papel.")
		print("> O jogador escolheu pedra.")
		print("=> O Computador ganhou!")
	elif opcaoComp == "tesoura":
		print("> O computador escolheu tesoura.")
		print("> O jogador escolheu pedra.")
		print("=> O Jogador ganhou!")
elif opcao == 2:
	if opcaoComp == "papel":
		print("> Ambos jogaram papel!")
		print("> EMPATE") 
	elif opcaoComp == "pedra":
		print("> O computador escolheu pedra.")
		print("> O jogador escolheu papel.")
		print("=> O Jogador ganhou!")
	elif opcaoComp == "tesoura":
		print("> O computador escolheu tesoura.")
		print("> O jogador escolheu papel.")
		print("=> O Computador ganhou!")
elif opcao == 3:
	if opcaoComp == "tesoura":
		print("> Ambos jogaram tesoura!")
		print("> EMPATE") 
	elif opcaoComp == "papel":
		print("> O computador escolheu papel.")
		print("> O jogador escolheu tesoura.")
		print("=> O Jogador ganhou!")
	elif opcaoComp == "pedra":
		print("> O computador escolheu pedra.")
		print("> O jogador escolheu tesoura.")
		print("=> O Computador ganhou!")
else:
	print("> ERRO")
	print("> Opção Inválida!")		
