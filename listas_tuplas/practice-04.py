lista_inventario = ['Pão', 'Leite', 'Ovos']

item_procurado = input('Digite o item que você quer verificar\t->')

if not item_procurado.title() in lista_inventario:
    print(f'O item {item_procurado} precisa ser comprado.')
else:
    print(f'O item {item_procurado} já se encontra disponível.')