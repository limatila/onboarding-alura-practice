
products = input("Digite os produtos (separados por vírgula): ").split(',')
prices = input("Digite os preços (separados por vírgula): ").split(',')


def clean_list(values_list: list[str]):
    return [value.strip() for value in values_list]

def map_products_to_prices(list_1: list[str], list_2: list[str]):
    return dict(zip(list_1, list_2))


products, prices = clean_list(products), clean_list(prices)

mapped_products = map_products_to_prices(products, prices)


print('')
for product, price in mapped_products.items():
    print(f"{product}: {price}")
