distancia = float(input(' Digite a distância da viagem em KM:'))
print(f' Você fará uma viagem de {distancia:.1f}Km.')

if distancia > 200:
	print(f' O custo da viagem é R${distancia*0.45}')
else:
	print(f' O custo da viagem é R${distancia*0.5}')
