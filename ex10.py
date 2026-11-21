################################################################
# Descrição: Conta os números ímpares e calcula seu percentual.
# Parâmetros de entrada: Dez valores numéricos inteiros.
# Valores de saída: Quantidade e percentual de números ímpares.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

A = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º número inteiro: "))
    A.append(valor)

quantidade_impares = 0

for valor in A:
    if valor % 2 != 0:
        quantidade_impares += 1

percentual = (quantidade_impares / len(A)) * 100

print(f"Total de números ímpares: {quantidade_impares}")
print(f"Percentual de números ímpares: {percentual:.2f}%")
