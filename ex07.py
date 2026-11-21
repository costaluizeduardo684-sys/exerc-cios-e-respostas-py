################################################################
# Descrição: Cria vetor B com a soma de 1 até cada valor de A.
# Parâmetros de entrada: Vinte valores inteiros para o vetor A.
# Valores de saída: Elementos calculados e armazenados no vetor B.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

A = []
B = []

for i in range(20):
    valor = int(input(f"Digite o {i + 1}º valor inteiro de A: "))
    A.append(valor)

    soma = 0
    contador = 1
    while contador <= valor:
        soma += contador
        contador += 1

    B.append(soma)

print("Elementos do vetor B:")
for valor in B:
    print(valor)
