
grades = input("Digite as notas dos alunos separadas por vírgula\t->").split(",")
grades = [
    float(grade.strip()) for grade in grades
]

sum_grades = sum(grades)
average_grade = sum_grades / len(grades) if grades else 0

print(f"\nMédia final da turma: {average_grade:.2f}")