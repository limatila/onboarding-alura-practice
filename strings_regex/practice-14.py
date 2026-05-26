
class Patient:
    first_name: str
    last_name: str
    year_of_birth: int | None

    def __init__(self, first_name, last_name, year_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
while True:
    text_for_collection = input("Digite o nome completo e o ano de nascimento do paciente\t->")

    try:
        names, year = text_for_collection.split(" - ")

        first_name, *last_name = names.title().strip().split()

        if len(year) != 4 or not year.isdigit():
            print(f"Ano de nascimento inválido: \'{year}\', tornando nulo.") 
            year = None
        else:
            year = int(year)

        patient = Patient(first_name, " ".join(last_name), year)
    except:
        print("\nEntrada inválida, tente novamente.")
        continue

    print(f'\nPrimeiro nome: {patient.first_name}')
    print(f'Sobrenome: {patient.last_name}')
    print(f'Ano de nascimento: {"Desconhecido" if (patient.year_of_birth is None) else patient.year_of_birth}')
    break