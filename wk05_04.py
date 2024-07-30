class Person:
    def __init__(self, name, age, address=None, phone_number=None):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def update_contact_info(self, address=None, phone_number=None):
        """Updates the address and/or phone number."""
        if address:
            self.address = address
        if phone_number:
            self.phone_number = phone_number

    def display_info(self):
        """Prints all attributes of the Person object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        if self.age >= 18:
            print("You're an adult now!")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")

my_info = Person(name="Cattleya", age=19)
my_info.update_contact_info(address="52/1 Moo5", phone_number="083-110-7840")
my_info.display_info()
my_info.have_birthday()
my_info.display_info()
