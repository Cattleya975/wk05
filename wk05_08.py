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

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.age >= 18:
            print("You are an adult.")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

    def greet(self):
        print(f"Hello, my name is {self.name}.")


    def set_salary(self, salary):
        self.__salary = salary


    def get_salary(self):
        return self.__salary


    @staticmethod
    def is_adult(age):
        return age >= 18

my_info = Person(name="Cattleya", age=19, address="KMITL", phone_number="090-989-6567")
age_to_check = 19
print(f"Is {age_to_check} an adult? {Person.is_adult(age_to_check)}")