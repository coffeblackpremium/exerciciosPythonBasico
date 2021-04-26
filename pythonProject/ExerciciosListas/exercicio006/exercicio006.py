"""
006)Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""
alunos = []
notas = []
media = 0

for aluno in range(10):
    novo_aluno = input('Digite o nome do Aluno: ')
    for nota in range(1, 5):
        nova_nota = float(input(f"Digite a {nota}°Nota do aluno: "))
        media += nova_nota
    media = media / 4
    if media >= 7:
        alunos.append([novo_aluno,media])
print(alunos)
