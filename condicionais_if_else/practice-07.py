
print("Cálculo de IMC - Índice de Massa Corporal")

try:
    height = float(input("Informe a altura (em metros, ex: 1.75)\t->"))
    weight = float(input("Informe o peso (em quilos)\t->"))
except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

if height <= 0 or weight <= 0:
    print("[ERRO] Por favor, informe valores positivos para altura e peso.")

imc_ranges = {
    (0, 18.5): "Abaixo do peso",
    (18.5, 24.9): "Peso normal",
    (25, 29.9): "Sobrepeso",
    (30, 34.9): "Obesidade grau 1",
    (35, 39.9): "Obesidade grau 2",
    (40, float('inf')): "Obesidade grau 3"
}

imc_result = weight / (height ** 2)

for (lower, upper), category in imc_ranges.items():
    if lower <= imc_result < upper:
        print(f"\nSeu IMC é: {imc_result:.2f} ")
        print(f"Você está classificado na categoria: {category}.")
        break
else:
    print("\nOcorreu uma inconsistência inesperada ao tentar calcular e interpretar o seu IMC.")