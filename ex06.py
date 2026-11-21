################################################################
# Descrição: Lê 20 temperaturas e calcula menor, maior e média.
# Parâmetros de entrada: Vinte valores reais em graus Celsius.
# Valores de saída: Menor temperatura, maior temperatura e média.
# Autor:                 Luiz Eduardo Santos Costa
################################################################

temperaturas = []

for i in range(20):
    temperatura = float(input(f"Digite a temperatura {i + 1} (°C): "))
    temperaturas.append(temperatura)

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"Menor temperatura: {menor:.2f} °C")
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Média das temperaturas: {media:.2f} °C")
