
from functools import reduce

valores = [10, 20, 30, 40, 50]

total_sum = reduce(lambda x, y: x + y, valores)

print(f"A soma total dos valores é: {total_sum}")