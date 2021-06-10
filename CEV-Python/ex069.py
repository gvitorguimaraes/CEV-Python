maiores = homens = mulheresSub20 = 0
while True:
    print("\n========================================")
    print("=         CADASTRE UMA PESSOA          =")
    print("========================================")
    
    idade = int(input(">> Idade: "))
    sexo = str(input(">> Sexo[F/M]: ")).upper().strip()
    continuar = str(input(">> Deseja continuar[S/N]?: ")).upper().strip()
    
    
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresSub20 += 1
    if continuar == "N":
        break    

print("========================================")
print(f">> Total de pessoas maiores de 18 anos: {maiores}")
print(f">> Total de homens: {homens}")
print(f">> Total de mulheres com menos de 20 anos: {mulheresSub20}")
print("\n>> Fim do programa!")