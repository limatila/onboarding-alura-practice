
try:
    apple_sales = int(input("Digite a quantidade de maçãs vendidas\t->"))
    banana_sales = int(input("Digite a quantidade de bananas vendidas\t->"))
except ValueError:
    print("Por favor, digite um número ao inserir as quantidades.")

result = ''

if apple_sales > banana_sales:
    result = "As maçãs tiveram mais vendas."
elif apple_sales < banana_sales:
    result = "As bananas tiveram mais vendas."
else: 
    result = "As maçãs e as bananas venderam a mesma quantidade."

if result:
    print(f"\n{result}")
else: raise Exception("Ocorreu um erro inesperado ao comparar as vendas.")

print("\nEnding process...")