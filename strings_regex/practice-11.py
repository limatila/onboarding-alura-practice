import re


nome_inserido = input("Digite o nome do cliente para validação\t->")

first_name_pattern= '^[A-ZÀ-Ý][a-zà-ÿ]+'

connectors_pattern = 'de|da|do|das|dos|e'
last_names_pattern = f'( ({connectors_pattern}|[A-ZÀ-Ý][a-zà-ÿ]+))*$'

valid_name_pattern = (first_name_pattern + last_names_pattern)

if re.match(valid_name_pattern, nome_inserido):
    print("Nome válido")
else:
    print("Nome inválido")
