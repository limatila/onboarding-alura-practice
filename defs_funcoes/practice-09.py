
values_to_measure = input("Digite os valores das vendas (separados por espaços): ")

def extract_even_numbers(values: str) -> str:
    try:
        numbers = set([x.strip() for x in values.split(' ')])
        even_numbers = list(filter(lambda x: int(x) % 2 == 0, numbers))
        return ' '.join(sorted(even_numbers))

    except ValueError:
        print("[ERROR] Por favor, insira numeros válidos para comparação.")
        return None
    
print(f"Números pares: {extract_even_numbers(values_to_measure)}")