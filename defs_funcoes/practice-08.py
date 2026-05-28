
values_to_sum = input("Digite os valores das vendas (separados por espaços): ")

def sum_typed_numbers(values: str) -> float:
    try:
        numbers = [float(x.strip()) for x in values.split(' ')]
        return sum(numbers)
    except ValueError:
        print("[ERROR] Por favor, insira numeros válidos para interpretação.")
        return None

print(f"O total de vendas foi: {sum_typed_numbers(values_to_sum):.2f}")
