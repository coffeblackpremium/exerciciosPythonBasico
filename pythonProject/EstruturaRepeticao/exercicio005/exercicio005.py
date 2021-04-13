"""
005)Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
while True:
    populacaoA, populacaoB = float(input('Digite a Quantidade Populacional de A: ')), 200000
    taxaA, taxaB = float(input('Digite quanto em Porcentagem de taxa: ')), 0.0015
    taxaA = taxaA / 100
    ano = 0
    if populacaoA > populacaoB:
        print('Valor Invalido!')
    else:
        while populacaoA < populacaoB:
            populacaoA = populacaoA * taxaA + populacaoA
            populacaoB = populacaoB * taxaB + populacaoB
            ano += 1
        print(f'A Populacão A ira ultrapassar a Populacao B em {ano} Anos')