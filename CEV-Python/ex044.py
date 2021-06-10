#Gerenciador de pagamentos
print("=== Gerenciador de Pagamentos ===\n")
preco = float(input("> Digite o preço do produto: R$"))
print("=========== Pagamento ===========\n")
print("=> [1] À Vista (dinheiro/Cheque) ") #10% desconto
print("=> [2] À Vista (Cartão)") #5% desconto
print("=> [3] 2x no Cartão") #Preço normal
print("=> [4] 3x ou mais no Cartão") #20% juros
print("\n=================================\n")
pagamento = int(input("> Opção de pagamento: "))

if pagamento == 1:
	print(f"\n> O valor a ser pago será R${(preco*0.90):.2f}")
elif pagamento == 2:
	print(f"\n> O valor a ser pago será R${(preco*0.95):.2f}")
elif pagamento == 3:
	print(f"\n> O valor a ser pago será R${preco:.2f}")
elif pagamento == 4:
	print(f"\n> O valor a ser pago será R${(preco*1.20):.2f}")
else:
	print(f"\n> Opção Inválida!")
