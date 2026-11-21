################################################################
# Descrição: Calcula o total de grãos de trigo em um tabuleiro.
# Parâmetros de entrada: Não há entrada de dados.
# Valores de saída: Quantidade de grãos em cada casa e total geral.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

graos = 1
total = 0

for casa in range(1, 65):
    print(f"Casa {casa}: {graos} grão(s)")
    total += graos
    graos *= 2

print(f"Total de grãos no tabuleiro: {total}")
