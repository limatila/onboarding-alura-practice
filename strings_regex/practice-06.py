
class Client:
    name: str
    city_name: str

    def __init__(self, name: str, city_name: str):
        self.name = name
        self.city_name = city_name

name_input = input("Digite o nome do cliente\t->")
city_input = input("Digite a cidade do cliente\t->")

client = Client(name_input, city_input)

print(f"Olá {client.name}! Bem-vinda ao sistema da cidade de {client.city_name}!")