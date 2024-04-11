#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

qnt = int(input("Quantidade de idades: "))
somaIdades = 0

for i in range(0,qnt):
    idade = int(input(f"Informe a {i+1}ª idade: "))
    somaIdades += idade

media = somaIdades/qnt
print(f"A média entre as idades é: {media}")