#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

divisores = []
numero = int(input("Informe um número inteiro positivo: "))

while numero < 0:
    numero = int(input("Número inválido\nDigite um número inteiro positivo: "))
    
for divisor in range(1,numero+1):
    if numero % divisor == 0:
        print(divisor)
        divisores.append(divisor)

print(50*"-")
print(f"O divisores de {numero} são: {divisores}")
print(50*"-")