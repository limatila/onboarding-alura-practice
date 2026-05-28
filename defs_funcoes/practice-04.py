
birth_year = input("Digite o ano de nascimento\t->")
current_year = input("Digite o ano atual\t->")

def calculate_age(birth_year, current_year):
    try:
        age = int(current_year) - int(birth_year)
        return age
    except ValueError:
        print("[ERRO] Por favor, certifique-se de que ambos os anos sejam números válidos.")
        exit(1)

age = calculate_age(birth_year, current_year)

print(f"A idade é {age} anos.")