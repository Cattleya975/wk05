class Person:
    def __init__(self, name, age, address=None, phone_number=None):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def update_contact_info(self, address=None, phone_number=None):
        if address:
            self.address = address
        if phone_number:
            self.phone_number = phone_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

class Student(Person):
    def __init__(self, name, age, student_id, address=None, phone_number=None):
        super().__init__(name, age, address, phone_number)
        self.student_id = student_id

my_student = Student(name="Cattleya", age=19, student_id="66010975", address="KMITL", phone_number="090-989-6567")
my_student.display_info()
print(f"Student ID: {my_student.student_id}")
