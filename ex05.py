################################################################
# Descrição: Calcula o quociente inteiro por subtrações sucessivas.
# Parâmetros de entrada: Dividendo e divisor inteiros.
# Valores de saída: Quociente inteiro da divisão.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Não é possível dividir por zero.")
else:
    sinal = 1
    if (dividendo < 0) != (divisor < 0):
        sinal = -1

    resto = abs(dividendo)
    divisor_abs = abs(divisor)
    quociente = 0

    while resto >= divisor_abs:
        resto -= divisor_abs
        quociente += 1

    print(f"Quociente inteiro: {sinal * quociente}")
