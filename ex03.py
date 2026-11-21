################################################################
# Descrição: Soma valores positivos e calcula média e quantidade.
# Parâmetros de entrada: Valores numéricos; um valor negativo encerra.
# Valores de saída: Somatório, média e total de valores informados.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

soma = 0.0
quantidade = 0

while True:
    valor = float(input("Digite um valor (negativo para encerrar): "))

    if valor < 0:
        break

    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(f"Somatório: {soma}")
print(f"Média: {media}")
print(f"Total de valores lidos: {quantidade}")
