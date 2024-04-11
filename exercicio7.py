#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

soma = 0

for i in range(0,100):
    if i % 2 == 0:
        soma += i

print(50*"-")
print(f"A soma dos 50 primeiros números pares é: {soma}")
print(50*"-")
#Considerei o 0 como o primeiro número par, então o 100 não é adicionado à conta
#Se o 100 fosse adicionado, o resultado da soma seria 2550