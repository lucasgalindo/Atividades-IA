preco = float(input("Digite o preço do produto: R$"))
condicao = int(input("Escolha a condição de pagamento (1-4): "))
if condicao == 1:
    preco_final = preco * 0.9
elif condicao == 2:
    preco_final = preco * 0.85
elif condicao == 3:
    preco_final = preco
elif condicao == 4:
    preco_final = preco * 1.1
print(f"O preço a pagar é R${preco_final:.2f}.")