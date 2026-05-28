
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

def convert_list_items_str_to_int(list_items):
    list_items = [int(item) for item in list_items]
    return list_items

telefones_convertidos = convert_list_items_str_to_int(telefones)
print(telefones_convertidos)

print("Todos os números foram convertidos corretamente!")