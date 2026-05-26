
estoque = { 
    "Caderno universitário": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
}

print('Estoque atual:')
for product, quantity in estoque.items():
    print(f" - {product}: {quantity}")

name = input(f"\nDigite o nome do produto a ser atualizado: ")
if not name in estoque.keys():
    print(f"\nProduto '{name}' não encontrado no estoque!")
    exit(1)

try:
    quantity = int(input(f"Digite nova quantidade do produto '{name}': "))
except ValueError:
    print("\n[ERRO] Por favor, digite um número válido ao inserir os valores.")
    exit(1)

estoque[name] = quantity
print(f"\nProduto '{name}' atualizado com sucesso! Nova quantidade: {quantity}.")

print('Estoque atual:')
for product, quantity in estoque.items():
    print(f" - {product}: {quantity}")
