"""
010)Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor_1 = [numero_vetor1 for numero_vetor1 in range(1, 10)]
vetor_2 = [numero_vetor2 for numero_vetor2 in range(11, 21)]
vetor3 = [ab for ab in zip(vetor_1, vetor_2)]
print(vetor3)
