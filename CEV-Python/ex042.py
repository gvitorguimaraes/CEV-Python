#Analisando triângulos V2
a = float(input("> Digite o valor do lado A: "))
b = float(input("> Digite o valor do lado B: "))
c = float(input("> Digite o valor do lado C: "))

if (a+b)>c and (a+c)>b and (c+b)>a:
	if a == b != c or a == c != b or c == b != a:
		print("> Essas medidas formam um triângulo ISÓCELES.")
	elif a != b != c:
		print("> Essas medidas formam um triângulo ESCALENO.")
	elif a == b == c:
		print("> Essas medidas formam um triângulo EQUILÁTERO.")
else:
	print("> Essas medidas NÃO podem formar um triângulo!")
