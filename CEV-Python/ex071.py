print("="*30)
print("{:^30}".format("BANCO MALADO"))
print("="*30)

valor = float(input(">> Quanto você deseja sacar: "))
totalCed = 0
ced = 50

while True:
    if valor >= ced:
        valor -= ced
        totalCed += 1
    else:
        print(f">> Total de cédulas de R${ced} é: {totalCed}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if valor == 0:
            break
