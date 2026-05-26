try:
    distance = float(input("Digite a distância percorrida (em km, ex: 200.00)\t->"))
except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

if distance < 0:
    print("[ERRO] A distância percorrida deve ser um número positivo.")
    exit(1)

grade_ranges = {
    (0, 99.9): 10.00,
    (100, 199.9): 20.00,
    (200, float('inf')): 30.00
}

for (lower, upper), category in grade_ranges.items():
    if lower <= distance < upper:
        print(f"Valor do pedágio: R${category:.2f}.")
        break
else:
    print("\nOcorreu uma inconsistência inesperada ao tentar interpretar o valor do pedágio.")