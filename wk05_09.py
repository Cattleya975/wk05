class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def greet(self):
        print(f"Hi, I'm {self.name}, and my student ID is {self.student_id}.")

def introduce(person_object):
    person_object.greet()

person = Person(name="Cattleya")
student = Student(name="Catt", student_id=66010975)

introduce(person)
introduce(student)
