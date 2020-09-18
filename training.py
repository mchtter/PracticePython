# ASAL SAYI HESAPLAMA
numberOne = int(input("Please input first number: "))
numberTwo = int(input("Please input second number: "))


def checkPrimeNumber():
    for prime in range(numberOne, numberTwo+1):
        if prime > 1:
            for number in range(2, prime):
                if prime % number == 0:
                    break
            else:
                print(prime)


checkPrimeNumber()





# TAM BÖLEN HESAPLAMA
inputNumber = int(input("Please enter number for divisor calculation: "))


def checkFactor(number):
    factorList = []

    for factor in range(2, number):
        if number % factor == 0:
            factorList.append(factor)
    print(factorList)
    return factorList


checkFactor(inputNumber)





# PARAMETRE LİSTELEME
someParameters = input("Please Enter some parameters: ")


def createList(*someParameters):
    paramList = []

    for add in someParameters:
        paramList.append(add)
    print(paramList)
    return paramList


createList(someParameters)





# BANKAMATİK
accountOne = {
    'nameSurname': 'Alperen ERYILMAZ',
    'number': '123456789',
    'balance': 6000,
    'additional': 6000
}
accountTwo = {
    'nameSurname': 'Mücahit ERYILMAZ',
    'number': '987654321',
    'balance': 3000,
    'additional': 5000
}
accountThree = {
    'nameSurname': 'Eryılmaz ERYILMAZ',
    'number': '1593572468',
    'balance': 1000,
    'additional': 3000
}


def withdrawMoney(key, value):
    print(f"Welcome, {key['nameSurname']}")

    if (key['balance'] >= value):
        key['balance'] -= value
        print(
            f"Money withdraw is Successfull! Remaining Balance: {key['balance']}")

    elif (key['balance'] < value):
        totalBalance = key['balance'] + key['additional']
        if totalBalance >= value:
            checkAdditional = input(
                "Do you want use Additional Account?(Y/N): ")
            if checkAdditional.upper() == "Y":
                additionalBalanceUsed = value - key['balance']
                key['balance'] = 0
                key['additional'] -= additionalBalanceUsed
                print(
                    f"Money withdraw is Successfull! (Additional) Total Balance: {key['additional']}")

            elif checkAdditional.upper() == "N":
                print(
                    f"Not Enough Account Balance {key['balance']}, Additional Account Balance is {key['additional']}")
        else:
            print(f"Not Enough Account Balance")


withdrawMoney(accountOne, 6000)
withdrawMoney(accountThree, 5000)





# NESNE TABANLI PROGRAMLAMA I
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





# NESNE TABANLI PROGRAMLAMA II
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





# SESLİ HARF SAYACI
vowelList = "aeıioöuü"
vowelMeter = 0
countWord = input("Please enter for word to count: ")

for word in countWord:
    if word in vowelList:
        vowelMeter += 1

if vowelMeter == 1:
    print(f"There are {vowelMeter} vowel in the word {countWord}.")
else:
    print(f"There are {vowelMeter} vowels in the word {countWord}.")
