
participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
}

print("Nomes dos participantes:", ", ".join(list(participantes.keys())))
print("Idades dos participantes:", ", ".join(str(age) for age in participantes.values()))

print("\nParticipantes e suas idades:")
for name, age in participantes.items():
    print(f"- {name}: {age} anos.")