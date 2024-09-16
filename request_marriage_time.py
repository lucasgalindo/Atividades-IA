nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil (CASADA/CASADO/OUTRO): ").upper()
if sexo == "F" and estado_civil == "CASADA":
    anos_casada = int(input("Quantos anos de casada? "))
    print(f"Tempo de casada: {anos_casada} anos.")
