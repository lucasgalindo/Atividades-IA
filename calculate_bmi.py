peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}.")
if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Peso normal.")
elif 25 <= imc < 30:
    print("Acima do peso.")
else:
    print("Obeso.")