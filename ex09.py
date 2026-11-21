################################################################
# Descrição: Lê e valida os vetores A e B e junta seus elementos.
# Parâmetros de entrada: 12 inteiros divisíveis por 2 ou 3 para A e
#                       12 inteiros que não sejam múltiplos de 5 para B.
# Valores de saída: Vetor C com os 24 elementos de A seguidos de B.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

A = []
B = []

print("Preenchimento do vetor A (valores divisíveis por 2 ou 3):")
while len(A) < 12:
    valor = int(input(f"Digite o {len(A) + 1}º valor de A: "))
    if valor % 2 == 0 or valor % 3 == 0:
        A.append(valor)
    else:
        print("Valor inválido. Digite um número divisível por 2 ou 3.")

print("\nPreenchimento do vetor B (valores que não sejam múltiplos de 5):")
while len(B) < 12:
    valor = int(input(f"Digite o {len(B) + 1}º valor de B: "))
    if valor % 5 != 0:
        B.append(valor)
    else:
        print("Valor inválido. O número não pode ser múltiplo de 5.")

C = A + B

print("\nElementos do vetor C:")
print(C)
