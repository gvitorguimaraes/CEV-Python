dado = input('Digite algo: ')

print(f'O tipo primitivo é: {type(dado)}')
print(f'É um dado numerico? {dado.isnumeric()}')
print(f'Só possui espaços? {dado.isspace()}')
print(f'É alfabético? {dado.isalpha()}')
print(f'É alfanumérico? {dado.isalnum()}')
print(f'Está em maiusculas? {dado.isupper()}')
print(f'Está em minúsculas? {dado.islower()}')
print(f'Está capitalizado? {dado.istitle()}')
