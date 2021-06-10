#Contagem regressiva
from time import sleep
print("==== Contagem para os fogos! ====")
for count in range(10, 0, -1):
	sleep(1)
	print(count)
sleep(1)
print("\n==== FOGOS! ====")
