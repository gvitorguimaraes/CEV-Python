#Alistamento militar
ano = int(input("> Digite o seu ano de nascimento: "))

idade = 2020-ano 
print(f"> Você tem {idade} anos.")
if idade == 18:
	print("> Você deve se alistar este ano!")
elif idade > 18:
	print(f"> Seu ano de alistamento foi {ano+18} você esta {idade-18} anos atrasado!")
else:
	print(f"> Seu ano de alistamento será {ano+18} ainda faltam {18-idade} anos!")
