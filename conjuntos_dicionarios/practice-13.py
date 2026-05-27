
class ShowReprAsStrMixin:
    def __repr__(self):
        return self.__str__()


class Category(ShowReprAsStrMixin):
    def __init__(self, name: str):
        self.name = name
        self.products: list['Product'] = []

    def __str__(self):
        return f"{self.name} - {len(self.products)} produtos"
    
    def add_product(self, product: 'Product'):
        self.products.append(product)
    
    def get_total_in_products(self):
        total_value = 0
        
        for product in self.products:
            total_value += product.total_value
        
        return total_value


class Product(ShowReprAsStrMixin):
    def __init__(self, name: str, quantity: int, unit_value: float):
        self.name = name
        self.quantity = quantity
        self.unit_value = unit_value

    def __str__(self):
        return f"{self.name}"
    
    @property
    def total_value(self):
        return self.quantity * self.unit_value


vendas = { 
    "Eletrônicos": [
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ],
    "Eletrodomésticos": [
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ],
    "Livros": [
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ]
}

sales_categories = []

for category, products in vendas.items():
    new_category = Category(category)
    for product in products:
        new_product = Product(product["produto"], product["quantidade"], product["valor_unitario"])
        new_category.add_product(new_product)
    
    sales_categories.append(new_category)

for category in sales_categories:
    print(f"- {category.name}: R$ {category.get_total_in_products():.2f}")
