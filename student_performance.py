numero_aluno = int(input("Digite o número do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media_exercicios = float(input("Digite a média dos exercícios: "))
    
media_aprov = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7
    
if media_aprov >= 90
    conceito = 'A'
elif 75 <= media_aprov < 90:
    conceito = 'B'
elif 60 <= media_aprov < 75:
    conceito = 'C'
elif 40 <= media_aprov < 60:
    conceito = 'D'
else:
    conceito = 'E'

print(f"Número do aluno: {numero_aluno}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media_exercicios}")
print(f"Média de aproveitamento: {media_aprov:.2f}")
print(f"Conceito: {conceito}")
    
if conceito in ['A', 'B', 'C']:
    print("Aprovado")
else:
    print("Reprovado")