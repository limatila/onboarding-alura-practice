import asyncio

class ShowNameInReprMixin:
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Course(ShowNameInReprMixin):
    def __init__(self, name: str, vacancies: int, enrolled_students: list = []):
        self.name = name
        self.vacancies = vacancies
        self.enrolled_students = enrolled_students


class Student(ShowNameInReprMixin):
    def __init__(self, name: str, course: Course):
        self.name: str = name
        self.course: Course = course

    async def check_course_availability(self):
        from random import randint
        await asyncio.sleep(randint(1, 3))
        course_to_subscribe = cursos[self.course.name]

        if len(course_to_subscribe["inscritos"]) >= course_to_subscribe["vagas"]:
            print(f"Turma lotada! {self.name} não pôde se inscrever no curso {self.course}.")
            return False
        
        elif self.name in course_to_subscribe["inscritos"]:
            print(f"Aluno {self.name} já está inscrito no curso {self.course}.")
            return False
        
        else:
            return True


cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}
 
alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]

transformed_courses = []
transformed_students = []

async def subscribe_student(student: Student):
    is_available = await student.check_course_availability()
    
    if is_available:
        cursos[student.course.name]["inscritos"].append(student.name)
        print(f"Aluno {student.name} inscrito com sucesso no curso {student.course}.")

async def main():
    print("* Iniciando processo de inscrição...\n")
    tasks = []

    for course_name, course_info in cursos.items():
        new_course = Course(course_name, course_info["vagas"], course_info["inscritos"])
        transformed_courses.append(new_course)

    for student in alunos:
        try:
            student_course = [course for course in transformed_courses if course.name == student["curso"]][0]        
        except IndexError:
            print(f"Curso {student['curso']} não encontrado para aluno {student['nome']}.")
            continue

        new_student = Student(student["nome"], student_course)
        transformed_students.append(new_student)
        
        tasks.append(subscribe_student(new_student))
    
    await asyncio.gather(*tasks)
    
    print("\n* Processo de inscrição concluído!")


#* RUN
asyncio.run(main())