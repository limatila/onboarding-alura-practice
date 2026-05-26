
guests_list = ["Alice", "Bob", "Charlie", "Eve"]

new_guest_name = input("Digite o nome do novo convidado\t->")
try:
    new_guest_position = int(input("Digite a posição na qual deseja inserir o convidado (1°, 2°, etc.)\t->"))
    guests_list.insert(new_guest_position - 1, new_guest_name)

except ValueError:
    print("Por favor, digite uma posição válida.")
except IndexError:
    print("Posição inválida.")

print("Lista de convidados atualizada:", guests_list)