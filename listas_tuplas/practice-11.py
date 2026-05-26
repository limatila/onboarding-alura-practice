
orders = input("Pedidos feitos (separados por vírgula)\t->").split(",")
orders = [order.strip() for order in orders]

print("\nPedidos feitos:", orders)
while True:
    input_remove_last_order = input("Deseja remover o último pedido? (s/n)\t->").strip().lower()
    if input_remove_last_order == "s":
        if orders:
            removed_order = orders.pop()
            print(f"Pedido '{removed_order}' removido.")
        else:
            print("Não há mais pedidos para remover.")

        print("\nPedidos feitos:", orders)
    
    elif input_remove_last_order == "n":
        break
    

print("\nPedidos finais:", orders)