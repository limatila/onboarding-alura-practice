
from datetime import time

try:
    hour = int(input("Digite a hora atual\t->"))
    minute = int(input("Digite os minutos atuais\t->"))
except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")

try:
    current_time = time(hour, minute)
except ValueError:
    print("[ERRO] Hora ou minuto inválidos. Certifique-se de que a hora esteja entre 0 e 23 e os minutos entre 0 e 59.")
    exit(1)

def salute_time_of_day(current_time):
    if current_time < time(hour=12, minute=0):
        return "Bom dia!"
    elif current_time < time(hour=18, minute=0):
        return "Boa tarde!"
    else:
        return "Boa noite!"

print(f"\n{salute_time_of_day(current_time)}")
