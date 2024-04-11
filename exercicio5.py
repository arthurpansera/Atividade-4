#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

pares = []
impares = []

for num in range(0,10):
    num = int(input(f"Digite o {num+1}º número: "))
    if num % 2 != 0:
        impares.append(num)
    else:
        pares.append(num)

print(50*"-")
print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")
print(50*"-")