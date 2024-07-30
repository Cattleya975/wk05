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
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

my_info = Person(name="Cattleya", age=19)
my_info.update_contact_info(address="55/5 moo5", phone_number="090-989-6567")
my_info.display_info()
