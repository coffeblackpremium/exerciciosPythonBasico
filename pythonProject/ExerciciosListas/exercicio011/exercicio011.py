"""
011)Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor_1 = [a for a in range(10)]
vetor_2 = [b for b in range(10, 21)]
vetor_3 = [c for c in range(21, 31)]
vetor_intercalado = [novo_vetor for abc in zip(vetor_1, vetor_2, vetor_3) for novo_vetor in abc]
print(vetor_intercalado)
