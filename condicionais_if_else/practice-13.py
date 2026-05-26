try:
    monthly_income = float(input("Digite o valor da renda mensal\t->"))
    monthly_installment = float(input("Digite o valor da parcela desejada  ->"))
except ValueError:
    print("Por favor, digite um número ao inserir as quantidades.")

#* 1° regra
if monthly_income < 2000: 
    print("\nInfelizmente, o empréstimo não pode ser concedido devido ao baixo valor da sua renda mensal.")
#* 2° regra
elif monthly_installment > (monthly_income * 0.3): 
    print("\nEmpréstimo negado: parcela acima de 30% da renda mensal.")
#* Sucesso
else:
    print("\nEmpréstimo aprovado!")

print("\nEnding process...")