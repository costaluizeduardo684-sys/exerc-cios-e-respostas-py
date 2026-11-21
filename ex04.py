################################################################
# Descrição: Calcula a área de cômodos e a área total da residência.
# Parâmetros de entrada: Nome, largura e comprimento de cada cômodo.
# Valores de saída: Área de cada cômodo e área total residencial.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

area_total = 0.0

while True:
    nome = input("Nome do cômodo: ")
    largura = float(input("Largura do cômodo (m): "))
    comprimento = float(input("Comprimento do cômodo (m): "))

    area = largura * comprimento
    area_total += area

    print(f"Área do(a) {nome}: {area:.2f} m²")

    continuar = input("Deseja calcular outro cômodo? (SIM/NÃO): ").strip().upper()
    if continuar in ("NÃO", "NAO"):
        break

print(f"Área total da residência: {area_total:.2f} m²")
