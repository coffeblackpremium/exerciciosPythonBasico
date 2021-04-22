"""
014)Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""
nota_1, nota_2 = float(input('Digite a primeira nota do aluno: ')), float(input('Digite a segunda nota do Aluno: '))
media = (nota_1 + nota_2) / 2

if media >= 9 or media <= 10:
    print(f'Você tirou a media {media}: Conceito A. APROVADO!!')
elif media >= 7.5 or media < 9:
    print(f'Você tirou a media {media}: Conceito B. APROVADO!!')
elif media >= 6 or media < 7.5:
    print(f'Você tirou a media {media}: Conceito C. APROVADO!!')
elif media >= 4 or media < 6:
    print(f'Você tirou a media {media}: Conceito D. APROVADO!!')
elif media < 4.0 and media > 0:
    print(f'Você tirou a media {media}: Conceito E. APROVADO!!')
else:
    print('REPROVADO!')
