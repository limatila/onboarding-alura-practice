names_list = ['Ana', 'João', 'Pedro']

name_to_replace = input("Digite o nome incorreto\t->")
replacement_name = input("Digite o nome correto\t->")

if not name_to_replace or not replacement_name:
    print("Por favor, preencha ambos os campos.")

if name_to_replace in names_list:
    index = names_list.index(name_to_replace)
    names_list[index] = replacement_name
else:
    print("\n[WARNING] O nome a ser substituído não foi encontrado na lista.")

print("\nLista de nomes atualizada:", names_list)