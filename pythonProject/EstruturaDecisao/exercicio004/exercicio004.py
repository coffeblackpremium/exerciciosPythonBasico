"""
004)Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra_digitada = input('Digite uma letra para Saber se é vogal ou consoante: ')

if letra_digitada.lower() == 'a' or letra_digitada.lower() == 'o' or \
        letra_digitada.lower() == 'e' or letra_digitada.lower() == 'i' or letra_digitada.lower() == 'u':
    print(f'{letra_digitada} é uma Vogal')
else:
    print(f'{letra_digitada} é uma Consoante')
