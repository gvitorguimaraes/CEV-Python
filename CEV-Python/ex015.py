kmPerc = float(input(' Kilometragem percorrida: '))
dias = int(input(' Dias alugados: '))

preco = (kmPerc*0.15)+(dias*60)

print(f' O cliente utilizou o carro por {dias} dias e rodou {kmPerc}Km\n O valor total a ser pago será R${preco:.2f}')
