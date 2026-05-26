from dataclasses import dataclass


@dataclass(slots=True) #* Cria uma classe imutável com atributos padronizados e tipados
class Student:
    name: str
    age: int
    grade: float

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student_data = input(
    "Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula\t->"
).split(",")

students_list = []

offset_counter = 3
while True:
    student_data = [data.strip() for data in student_data]
    
    start_offset = offset_counter - 3
    new_student_data = student_data[start_offset:offset_counter]

    if not new_student_data:
        print("[SUCCESS] Encerrando a coleta de dados.")
        break
    elif not new_student_data or len(new_student_data) < 3:
        print(f"[WARNING] Dados insuficientes para criar um novo aluno a partir do index {start_offset} -- Encerrando a coleta de dados.")
        break
    
    try:
        student_name = new_student_data[0]
        student_age = int(new_student_data[1])
        student_grade = float(new_student_data[2])
    
        new_student = Student(student_name, student_age, student_grade)
        students_list.append(new_student)
    except ValueError as err:
        print(f"[ERROR] Erro ao criar aluno com dados: {new_student_data}")
        break

    offset_counter += 3

print("\nDados dos alunos:")
for student in students_list:
    print(f"Nome: {student.name}, Idade: {student.age}, Nota: {student.grade}")