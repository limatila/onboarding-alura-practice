
participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
}

print("Participantes dos workshops:")
for workshop, participants in participantes.items():
    print(f"- {workshop}: {', '.join(participants)}")

participant_to_remove = input("\nNome do participante a ser removido\t->")

is_updated = False
for workshop, participant_set in participantes.items():
    if participant_to_remove in participant_set:
        participant_set.remove(participant_to_remove)
        is_updated = True
        print(f"\nParticipante '{participant_to_remove}' removido com sucesso do workshop '{workshop}'!")
else:
    print(f"\nParticipante '{participant_to_remove}' não foi encontrado em nenhum workshop.")

if is_updated:
    print("Lista atualizada de participantes:")
    for workshop, participants in participantes.items():
        print(f"- {workshop}: {', '.join(participants)}")