
laura_list = input("Lista de Laura\t->")
ana_list = input("Lista de Ana\t->")

laura_set = set(laura_list.lower().split())
ana_set = set(ana_list.lower().split())

common_words = laura_set.intersection(ana_set)
laura_exclusive_itens = laura_set.difference(ana_set)
ana_exclusive_itens = ana_set.difference(laura_set)


print("\nItens em ambas as listas:", common_words)
print("\nItens exclusivos de Laura:", laura_exclusive_itens)
print("\nItens exclusivos de Ana:", ana_exclusive_itens)