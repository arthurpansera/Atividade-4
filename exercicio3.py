#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

valor = int(input("Digite um valor entre 1 e 10: "))

while valor < 1 or valor > 10:
    valor = int(input("Valor inválido\nDigite um valor entre 1 e 10: "))

if valor >= 1 and valor <= 10:
    print(f"Tabuada de {valor}")
    for i in range(1,11):
        print(f"{valor} x {i} = {valor*i}")