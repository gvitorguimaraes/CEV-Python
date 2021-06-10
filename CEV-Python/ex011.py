#Calculadora de tinta
largura = float(input(' Digite a largura da parede: '))
altura = float(input(' Digite a altura da parede: '))

area = largura*altura
litrosTinta = area/2

print(f' A sua parede tem dimensão de {largura}x{altura} portanto, uma área de {area:.2f}m2.\n Serão necessários {litrosTinta:.2f}L de tinta para pinta-la completamente.')
