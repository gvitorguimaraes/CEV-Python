menorValor = total = maisMil = prodBarato = 0

print("\n========================================")
print("=          LOJA SUPER BARATÃO          =")
print("========================================")

while True:

    produto = str(input("\n>> Produto: "))
    preco = float(input(">> Preço: R$"))
    continuar = str(input(">> Deseja adicionar mais produtos? (S/N): ")).upper().strip()

    total += preco

    if preco > 1000:
        maisMil += 1
    if menorValor != 0:
        if preco < menorValor:
            menorValor = preco
            prodBarato = produto 
    else:
        menorValor = preco
        prodBarato = produto
    if continuar != "S":
        break

print("================= FIM ==================")
print(f">> O preço total da compra é: R${total}")
print(f">> Temos {maisMil} produto custando mais de R$1000.00")
print(f">> O produto mais barato foi {prodBarato} que custa R${menorValor}")