from math import sqrt

catOposto = float(input(' Digite o comprimento do cateto oposto: '))
catAdjacente = float(input(' Digite o comprimento do cateto adjacente: '))

hipot = sqrt(catOposto**2 + catAdjacente**2)

print(f' A hipotenusa deste triângulo é {hipot:.2f}')
