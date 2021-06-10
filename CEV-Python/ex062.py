print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=       GERADOR DE PA       =")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

pa = int(input(">> Digite o termo inicial: "))
r = int(input(">> Digite a razão: "))
i = 1
termos = 10

while i <= termos:
	print(f" {pa} →", end='')
	pa += r
	i += 1
print(" Pausa!")

opcao = int(input(">> Deseja mostrar mais quantos termos? "))

while opcao > 0:
	termos = i + opcao
	while i < termos:
		print(f" {pa} →", end='')
		pa += r
		i += 1
	print(" Pausa")
	opcao = int(input(">> Deseja mostrar mais quantos termos? "))

print("---"*18)
print(f">> Fim do programa, foram exibidos {i-1} termos da PA!")
