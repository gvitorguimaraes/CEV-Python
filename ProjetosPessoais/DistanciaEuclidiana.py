#Distancia euclidiana
from math import sqrt
for loop in range(0, 99):
	X1 = float(input())
	Y1 = float(input())
	X2 = float(input())
	Y2 = float(input())
	if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
		print("0.00")
		break
	else:
		d = sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
		print(f'{d:.2f}')

