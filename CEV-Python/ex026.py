frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes nessa frase.')
fraseSep = frase.split()
print(f'A letra A aparece primeiro na posição {frase.find("A")+1}')
print(f'A letra A aparece pela ultima vez na posição {frase.rfind("A")+1}')
