
try:
    a_activity_days = int(input("Informe os dias para a atividade A\t->"))
    b_activity_days = int(input("Informe os dias para a atividade B\t->"))
    c_activity_days = int(input("Informe os dias para a atividade C\t->"))
except ValueError:
    print("Por favor, digite um número válido ao inserir as quantidades.")

for activity, days in zip(['A', 'B', 'C'], [a_activity_days, b_activity_days, c_activity_days]):
    if days < 0:
        print(f"\nErro: Os dias não podem ser negativos")
        break
else:
    activity_days_sum = a_activity_days + b_activity_days + c_activity_days
    print(f'\nSoma total dos dias trabalhados nas atividades: {activity_days_sum} dias.')

print("\nEnding process...")