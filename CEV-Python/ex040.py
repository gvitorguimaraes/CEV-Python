#Media de notas
nota1 = float(input("> Digite a primeira nota: "))
nota2 = float(input("> Digite a segunda nota: "))

media = (nota1+nota2)/2
print(f"> Sua média foi de {media} pontos")
if media >= 7:
	print("> Você foi APROVADO!")
elif 6.9 >= media >= 5:
	print("> Você está de RECUPERAÇÃO!")
else:
	print("> Você foi REPROVADO!")  
