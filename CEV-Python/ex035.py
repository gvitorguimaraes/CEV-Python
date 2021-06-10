a = float(input(' Digite o valor do segmento A: '))
b = float(input(' Digite o valor do segmento B: '))
c = float(input(' Digite o valor do segmento C: '))

if (b-c)< a <b+c and (a-c)< b <a+c and (a-b)< c <a+b:
	print(f' Os segmentos {a}, {b} e {c} PODEM formar um triângulo!')
else:
	print(f' Os segmentos {a}, {b} e {c} NÃO PODEM formar um triângulo!')

