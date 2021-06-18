class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def calculateEnvironment(self):
        return 2 * self.pi * self.radius

    def calculateArea(self):
        return self.pi * (self.radius ** 2)


c1 = Circle()
c2 = Circle(5)

print(
    f" c1 Area is : {c1.calculateArea()} and Environment {c1.calculateEnvironment()}")
print(
    f" c2 Area is : {c2.calculateArea()} and Environment {c2.calculateEnvironment()}")
