#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

listaNumeros = []

for i in range(0,10):
    numero = int(input(f"Informe o {i+1}º número: "))
    listaNumeros.append(numero)

listaNumeros.sort()
print(50*"-")
print(listaNumeros)
print(50*"-")