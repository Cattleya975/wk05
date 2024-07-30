class Person:
    def __init__(self, name, age, address=None, phone_number=None):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.__salary = None

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
        print(f"Salary: ${self.__salary}")

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

my_info = Person(name="Cattleya", age=19, address="KMITL", phone_number="090-989-6567")
my_info.set_salary(25000)
my_info.display_info()
