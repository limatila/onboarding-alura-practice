class Book:
    title: str
    stock_quantity: int

    def __init__(self, title, quantity):
        self.title = title
        self.stock_quantity = quantity

    def sell_from_stock(self):
        if self.stock_quantity <= 0:
            print("Estoque esgotado.")
            exit(0)
        else:
            self.stock_quantity -= 1

book = Book("O Ceifador", 5)

while True:
    book.sell_from_stock()
    print(f"Venda realizada! Estoque restante: {book.stock_quantity}")