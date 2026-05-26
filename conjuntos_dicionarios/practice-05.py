
first_text = input("Digite o Texto 1\t->")
text_to_compare = input("Digite o Texto 2\t->")

first_set = set(first_text.lower().split())
second_set = set(text_to_compare.lower().split())

common_itens = first_set.intersection(second_set)

print("\nPalavras em comum:", common_itens)