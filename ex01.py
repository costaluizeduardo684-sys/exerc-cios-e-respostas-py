################################################################
# Descrição: Apresenta as potências de base 3, do expoente 0 ao 15.
# Parâmetros de entrada: Não há entrada de dados.
# Valores de saída: Potências de 3 calculadas sem usar exponenciação.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

potencia = 1

for expoente in range(16):
    print(f"3 elevado a {expoente} = {potencia}")
    potencia *= 3
