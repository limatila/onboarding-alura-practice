
list_products: list[dict[str, str | int]] = []

for i in range(3):
    name = input(f"Digite o nome do {i+1}° produto\t->")
    try:
        quantity = int(input(f"Digite a quantidade do {i+1}° produto\t->"))
    except ValueError:
        print("\n[ERRO] Por favor, digite um número válido ao inserir os valores.")
        exit(1)

    product = {
        "name": name,
        "quantity": quantity
    }

    list_products.append(product)
    print('')

print("\nProdutos adicionados:")
for product in list_products:
    print(f"Nome: {product['name']}, Quantidade: {product['quantity']}")
