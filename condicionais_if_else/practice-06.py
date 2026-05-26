
try:
    current_temperature = float(input("Informe a temperatura atual\t->"))
except ValueError:
    print("Por favor, digite um número válido ao inserir a temperatura.")

if current_temperature > 25:
    print("\n[ALERTA] Temperatura acima do limite permitido.")

print("\nEnding process...")