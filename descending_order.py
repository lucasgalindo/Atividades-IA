valores = []
for i in range(3):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)
valores.sort(reverse=True)
print("Valores em ordem decrescente:", valores)