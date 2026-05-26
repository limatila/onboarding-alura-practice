try:
    first_grade = float(input("Digite a primeira nota\t->"))
    second_grade = float(input("Digite a primeira nota\t->"))
    third_grade = float(input("Digite a primeira nota\t->"))
except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

for activity, grade in zip(['primeira', 'segunda', 'terceira'], [first_grade, second_grade, third_grade]):
    if grade < 0 or grade > 10:
        print(f"\nErro: a nota {activity} deve estar entre 0 e 10.")
        exit(1)

grade_ranges = {
    (0, 5.9): "Reprovado",
    (6, 6.9): "Recuperação",
    (7, 10): "Aprovado"
}

all_grades = [first_grade, second_grade, third_grade]
grade_result = sum(all_grades) / len(all_grades)

for (lower, upper), category in grade_ranges.items():
    if lower <= grade_result < upper:
        print(f"\nMédia: {grade_result:.2f} ")
        print(f"Seu resultado: {category}.")
        break
else:
    print("\nOcorreu uma inconsistência inesperada ao tentar calcular e interpretar a média total.")