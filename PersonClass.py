class Person:
    address = "No information"

    def __init__(self, name, year):

        self.name = name
        self.year = year
        print("__init__ Method is activated.")

    def intro(self):
        print("Hello There, My name is " + self.name)

    def calculateAge(self):
        return 2020 - self.year


class Student(Person):
    pass


p1 = Person("Alperen", 1996)
p2 = Person("Mücahit", 1997)

p1.name = "Change Name"
p1.address = "Antalya"
p1.year = 1989

print(
    f"p1 name : {p1.name} and p1 year : {p1.year}. Address is : {p1.address}")
print(
    f"p2 name : {p2.name} and p2 year : {p2.year}. Address is : {p2.address}")

p1.intro()
print(f"Age is : {p1.calculateAge()}")
p2.intro()
print(f"Age is : {p2.calculateAge()}")
