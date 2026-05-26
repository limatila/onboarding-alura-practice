
participants_count = int(input("Quantos participantes o concurso teve?\t->"))

print(f"Primeiro, insira {participants_count} notas de cada participante:")

grades = []
for i in range(participants_count):
    new_grade = float(input(f"Nota do participante {i + 1}\t->"))
    grades.append(new_grade)

sorted_grades = sorted(grades)

print('Notas ordenadas:', sorted_grades)
