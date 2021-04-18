"""
004)Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes
"""
vetor = [input('Digite no maximo 10 Caracteres: ') for item in range(1)]
if len(vetor) > 10:
    print('Digitou mais que 10 Caracteres')
letraConsoante = 0
todas_vogais = []
for vet in vetor:
    for letra in vet:
        if letra.lower() == 'a':
            letraConsoante += 1
            todas_vogais.append(letra)
        elif letra.lower() == 'e':
            letraConsoante += 1
            todas_vogais.append(letra)
        elif letra.lower() == 'i':
            letraConsoante += 1
            todas_vogais.append(letra)
        elif letra.lower() == 'o':
            letraConsoante += 1
            todas_vogais.append(letra)
        elif letra.lower() == 'u':
            letraConsoante += 1
            todas_vogais.append(letra)
print(f'Todas as Letras Consoantes dessas palavras são: {letraConsoante}\n', 'E as Vogais sao ', *todas_vogais)
