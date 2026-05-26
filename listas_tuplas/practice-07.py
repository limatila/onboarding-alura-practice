
stock = ()
for i in range(2):
    new_stock = input(f"Produtos do estoque {i+1} (separados por vírgula)\t->")
    new_stock_tuple = tuple(product.strip() for product in new_stock.split(","))

    stock += new_stock_tuple

print('\nEstoque combinado:\n', stock)