#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

listaPares = []

for i in range(1,101):
    if i % 2 == 0:
        print(f"O número {i} é par")
        listaPares.append(i)

print(50*"-")
print(f"Os números pares são: {listaPares}")