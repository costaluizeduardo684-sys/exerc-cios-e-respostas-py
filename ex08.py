################################################################
# Descrição: Gera o vetor B conforme a paridade dos índices de A.
# Parâmetros de entrada: Quinze valores reais para o vetor A.
# Valores de saída: Elementos transformados e armazenados no vetor B.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

A = []
B = []

for i in range(15):
    valor = float(input(f"Digite o {i + 1}º valor de A: "))
    A.append(valor)

    indice = i + 1
    if indice % 2 == 0:
        B.append(valor / 2)
    else:
        B.append(valor * 1.5)

print("Elementos do vetor B:")
for valor in B:
    print(valor)
