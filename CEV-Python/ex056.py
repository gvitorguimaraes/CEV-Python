#Analisador completo
femSub20 = 0
idadeTotal = 0
idadeAnt = 0
nomeVelho = 0

for x in range(0, 4):
	print(f"\n=-=-=-=-= {x+1}° Pessoa =-=-=-=-=\n")
	nome = input("=> Nome: ").strip()
	
	idade = int(input("=> Idade: "))
	idadeTotal = idadeTotal + idade
	
	sexo = input("=> Sexo [M/F]: ").strip().upper()
	if sexo == 'F' and idade < 20:
		femSub20 += 1
	
	if x == 0 and sexo == 'M':
		idadeAnt = idade
		nomeVelho = nome
	else:
		if idadeAnt < idade:
			idadeAnt = idade
			nomeVelho = nome

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
print(f"=> A idade média é: {idadeTotal/4}")
print(f"=> O Homem mais velho é {nomeVelho} que tem {idadeAnt} anos")
print(f"=> Neste grupo existem {femSub20} mulheres com menos de 20 anos.")
