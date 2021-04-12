"""
003)Faça um Programa que verifique se uma letra digitada
é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra_digitada = input('Digite (F) para feminino e (M) para Masculino: ')

if letra_digitada.lower() == 'f':
    print('Seu sexo é Feminino')
elif letra_digitada.lower() == 'm':
    print('Seu sexo é masculino')
else:
    print('Sexo invalido!')
