try:
    total_spent = float(input("Digite o total de despesas do mês (R$)\t->"))
except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

if total_spent > 3000:
    print("Atenção! Você ultrapassou o limite do orçamento.")