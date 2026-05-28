
try:
    discount_percent = float(input("Digite a porcentagem de desconto\t->").strip())
    purchase_initial_value = float(input("Digite o valor da compra\t->").strip())

except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

def calculate_discount(discount_percent: float, purchase_initial_value: float) -> float:
    discount_amount = (discount_percent / 100) * purchase_initial_value
    final_price = purchase_initial_value - discount_amount
    
    return final_price


final_total_price = calculate_discount(discount_percent, purchase_initial_value)
print(f"\nPreço final com desconto: R${final_total_price:.2f}")
