"""
011)Altere o programa anterior para mostrar no final a soma dos números.
"""
numero_inteiro1, numero_inteiro2 = float(input('Digite um numero: ')), float(input('Digite outro numero: '))
lista = []

if numero_inteiro1 < numero_inteiro2:
    while numero_inteiro1 <= numero_inteiro2:
        numero_inteiro1 += 1
        if numero_inteiro1 == numero_inteiro2:
            break
        lista.append(numero_inteiro1)

if numero_inteiro2 < numero_inteiro1:
    while numero_inteiro2 <= numero_inteiro1:
        numero_inteiro2 +=1
        if numero_inteiro2 == numero_inteiro1:
            break
        lista.append(numero_inteiro2)

print(f'A soma do numero dos intervalo é {lista}O Resultado da soma dos números é: {sum(lista)}')