#Atividade 4: Exercícios (Repetição)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

listaSim = []
listaNao = []

for num in range(0,10):
    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20:
        print("O número está no intervalo")
        listaSim.append(num)
        print(50*"-")
    else:
        print("O número está fora do intervalo")
        listaNao.append(num)
        print(50*"-")

print(f"Os números que estão no intervalo [10,20] são: {listaSim}")
print(f"Os números ques tão fora do intervalo [10,20] são: {listaNao}")