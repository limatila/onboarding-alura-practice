
try:
    number = int(input("Digite um número\t->").strip())

except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")


def sum_numbers_1_to_n(n: int) -> int:
    if n == 1: return 1
    return n + sum_numbers_1_to_n(n - 1)


print(f"A soma de 1 a {number} é: {sum_numbers_1_to_n(number)}")
