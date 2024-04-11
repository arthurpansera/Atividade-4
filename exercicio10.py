#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

lista = [2,4,7,2,3,3,1,0,2,6]
numRepetido = 0
contRepetido = 0

for num in lista:
    cont = lista.count(num)
    if cont > contRepetido:
        numRepetido = num
        contRepetido = cont

print(50*"-")
print(f"O número que se repete mais vezes é: {numRepetido}")
print(50*"-")