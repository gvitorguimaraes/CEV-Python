#IMC
peso = float(input("> Digite seu peso (Kg): "))
altura = float(input("> Digite sua altura (m): "))
imc = peso/(altura**2)

print(f"> Seu IMC é {imc:.2f}")
if imc < 18.5:
	print("> Atenção! Você está abaixo do peso ideal.")
elif 18.5 <= imc < 25:
	print("> Ótimo! Você está no peso ideal.") 
elif 25 <= imc < 30:
	print("> Ok! Você está um pouco acima do peso.")
elif 30 <= imc < 40:
	print("> Atenção! Você está obeso.")
else:
	print("> ALERTA! Você está em obesidade MÓRBIDA")
