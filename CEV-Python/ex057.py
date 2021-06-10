#Verificar o sexo
sexo = input("=> Digite seu sexo: ").upper().strip()[0]

while sexo not in 'MnFf':
	print("ERRO! Opção inválida.")
	sexo = input("=> Digite seu sexo: ").upper().strip()[0]

print("Tudo certo!")
