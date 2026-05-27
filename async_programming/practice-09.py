import asyncio 

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def process_order(order):
    print(f"\nProcessando pedido {order['id']}...")
        
    if not order["pagamento_aprovado"]:
        print(f"Pagamento recusado para pedido {order['id']} Pedido cancelado.")
        return
    else:
        print(f"Pagamento aprovado para pedido {order['id']}.")
    
    if not order["estoque_disponivel"]:
        print(f"Estoque indisponível para pedido {order['id']} Pedido cancelado.")
        return
    else:
        print(f"Estoque disponível para pedido {order['id']}.")
    
    print(f"Pedido {order['id']} processado com sucesso!")

async def main():
    print("* Iniciando processamento de pedidos...")
    
    tasks = [process_order(order) for order in pedidos]
    await asyncio.gather(*tasks)
    
    print("\n* Todos os pedidos foram processados!")

asyncio.run(main())