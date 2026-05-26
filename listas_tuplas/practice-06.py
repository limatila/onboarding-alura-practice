
names_list = []

while True:
    new_name = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if new_name.lower() == 'sair':
        break
    names_list.append(new_name)

if names_list:
    print("\nVoluntários registrados:", names_list)
else:
    print("\nNenhum voluntário registrado.")