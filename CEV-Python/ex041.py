#Classificar atletas
ano = int(input("> Ano de nascimento: "))
idade = 2020-ano

print(f"> O atleta tem {idade} anos")
if idade <= 9:
	print("> Categoria => Mirim")
elif 9 < idade <= 14:
	print("> Categoria => Infantil")  
elif 14 < idade <= 19:
	print("> Categoria => Junior")
elif 19 < idade <= 25:
	print("> Categoria => Sênior")
else:
	print("> Categoria => Master")
