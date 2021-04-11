"""
004)Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
notas = []
for nota in range(1, 5):
    nota_aluno = float(input(f'Digite a {nota}° nota do Aluno: '))
    notas.append(nota_aluno)
media = (sum(notas) / 4)
print(f'A nota dos alunos foram {notas} e a média é {media}')
