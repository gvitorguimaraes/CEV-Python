from random import shuffle

alu1 = input(' Primeiro aluno: ')
alu2 = input(' Segundo aluno: ')
alu3 = input(' Terceiro aluno: ')
alu4 = input(' Quarto aluno: ')

alunos = [alu1, alu2, alu3, alu4]
shuffle(alunos)

print(f' A ordem de apresentação será: {alunos}')
