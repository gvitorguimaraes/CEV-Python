from time import sleep

a = int(input('> Digite um número: '))
sleep(0.5)
b = int(input('> Digite outro número: '))
sleep(0.5)

soma = a+b
sub = a-b
mult = a*b
div = a/b

sleep(1)
print(f'\n> A soma desses numeros é {soma}\n> A subtração é {sub}\n> O produto é {mult}\n> A divisão é {div:.3f}')
sleep(5)

c = int(input('\n> Digite outro numero:'))
d = int(input('> Digite o expoente: '))
sleep(0.5)
pot = c**d
sleep(1)

print(f'\n> O número {c} elevado a {d} é {pot}')
sleep(20) 
