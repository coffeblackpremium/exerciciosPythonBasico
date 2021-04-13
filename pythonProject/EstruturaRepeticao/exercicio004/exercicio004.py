"""
004)Supondo que a população de um país A seja da ordem de 80000
habitantes com uma taxa anual de crescimento de 3% e que a população de B
seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
calcule e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""
populacaoA, populacaoA = 80000, 200000
taxaA, taxaB = 0.03, 0.0015
ano = 0
while populacaoA < populacaoB:
    populacaoA = populacaoA * taxaA + populacaoA
    populacaoB = populacaoB * taxaB + populacaoB
    ano += 1

print(f'A Populacao A vai ultrapassar a Populacao B em {ano} anos')
