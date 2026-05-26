
guests_set = set()

while True:
    new_guest = input("Digite o nome do voluntário (ou 'sair' para encerrar)\t->")
    if new_guest.lower().strip() == 'sair':
        break
    guests_set.add(new_guest)

print("\nConvidados confirmados:", guests_set)