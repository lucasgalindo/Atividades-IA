valor1 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO: ")))
valor2 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO: ")))
if valor1 and valor2:
    print("Ambos são VERDADEIROS.")
elif not valor1 and not valor2:
    print("Ambos são FALSOS.")
else:
    print("São diferentes.")