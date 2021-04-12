"""
010)Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno_estudo = input('Digite o Seu turno de estudo: ')

if turno_estudo.lower() == 'm':
    print('Bom Dia!!')
elif turno_estudo.lower() == 'v':
    print('Boa Tarde!!')
elif turno_estudo.lower() == 'n':
    print('Boa Noite!')
else:
    print('Valor invalido!')
