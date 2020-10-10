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





# QUIZ APP (Quizzy)
class Questions:
    def __init__(self, questionText, questionAnswer, choiceList):
        self.questionText   = questionText
        self.questionAnswer = questionAnswer
        self.choiceList     = choiceList


    def answerCheck(self, answer):
        return self.questionAnswer == answer


class Quiz:
    def __init__(self, questionText):
        self.questionText = questionText
        self.score = 0
        self.questionIndex = 0


    def getQuestion(self):
        return self.questionText[self.questionIndex]


    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.questionText}')
        
        for q in question.choiceList:
            print("-" + q)

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.answerCheck(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questionText) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Score: {self.score}")
    
    def displayProgress(self):
        totalQuestion = len(self.questionText)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print("Quiz OVER!")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, '*'))


q01 = Questions('Where is the capital of Turkey?',              'Ankara',       ['Izmir',        'Istanbul',   'Ankara',        'Diyarbakır', 'Erzurum'])
q02 = Questions('Where is the capital of United States?',       'Washington DC',['Washington DC','New York',   'Seattle',       'Miami',      'Los Angeles'])
q03 = Questions('Where is the capital of United Kingdom?',      'London',       ['Oxford',       'Manchester', 'London',        'Cambridge',  'Liverpool'])
q04 = Questions('Where is the capital of Germany?',             'Berlin',       ['Munih',        'Berlin',     'Frankfurt',     'Hamburg',    'Köln'])
q05 = Questions('Where is the capital of Belgium?',             'Brussels',     ['Hasselt',      'Brugge',     'Anvers',        'Brussels',   'Halle'])
q06 = Questions('Where is the capital of Brazil?',              'Brasilia',     ['Brasilia',     'Salvador',   'Rio de Janeiro','São Paulo',  'Santo Andrê'])
q07 = Questions('Where is the capital of Egypt?',               'Cairo',        ['Ismailiye',    'Luksor',     'Asuan',         'Dimyat',     'Cairo'])
q08 = Questions('Where is the capital of Iraq?',                'Baghdad',      ['Erbil',        'Musul',      'Kerkuk',        'Baghdad',    'Basra'])
q09 = Questions('Where is the capital of Israel?',              'Tel Aviv',     ['Netanya',      'Tel Aviv',   'Hayfa',         'Tiberya',    'Akka'])
q10 = Questions('Where is the capital of Mexico?',              'Mexico City',  ['Mexico City',  'Guadalajara','Cancùn',        'Monterrey',  'Tijuana'])
q11 = Questions('Where is the capital of Netherlands?',         'Amsterdam',    ['Lahey',        'Rotterdam',  'Amsterdam',     'Utrecht',    'Maastricht'])
q12 = Questions('Where is the capital of Russia?',              'Moscow',       ['Petersburg',   'Soçi',       'Vladivostok',   'Moscow',     'Volgograd'])
q13 = Questions('Where is the capital of Uzbekistan?',          'Tashkent',     ['Buhara',       'Tashkent',   'Semekand',      'Tirmiz',     'Namangan'])
q14 = Questions('Where is the capital of Sweden?',              'Stockholm',    ['Visby',        'Göteborg',   'Malmö',         'Helsingborg','Stockholm'])
q15 = Questions('Where is the capital of Turkmenistan?',        'Ashgabat',     ['Daşoğuz',      'Türkmenabat','Ashgabat',      'Balkanabat', 'Atamurat'])
q16 = Questions('Where is the capital of Ukraine?',             'Kiev',         ['Lviv',         'Odessa',     'Harkov',        'Kiev',       'Çernivtsi'])
q17 = Questions('Where is the capital of United Arab Emirates?','Abu Dhabi',    ['Dubai',        'Sharjah',    'Abu Dhabi',     'Qaiwain',    'Fujairah'])
q18 = Questions('Where is the capital of Philippines?',         'Manila',       ['Manila',       'Quezon City','Makati',        'Cebu City',  'Baguio'])
q19 = Questions('Where is the capital of Pakistan?',            'Islamabad',    ['Lahor',        'Islamabad',  'Peşaver',       'Multan',     'Ketta'])
q20 = Questions('Where is the capital of Lebanon?',             'Beirut',       ['Trablusşam',   'Sayda',      'Beirut',        'Sur',        'Tyre'])
questionText = [q01, q02, q03, q04, q05, q06, q07, q08, q09, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]


quiz = Quiz(questionText)
test = quiz.getQuestion()
index = quiz.questionIndex

quiz.loadQuestion()



# QUIZ APP (Quizzy)
class Question:
    def __init__(self, questionText, questionAnswer, answerChoices):
        self.questionText   = questionText
        self.questionAnswer = questionAnswer
        self.answerChoices  = answerChoices
    
    def answerCheck(self, questionAnswer):
        return self.questionAnswer == questionAnswer
    
class Quiz:
    def __init__(self, questionList):
        self.questionList = questionList



q01 = Question('Where is the capital of Turkey?',         'Ankara',        ['Ankara',        'Istanbul',   'Izmir',     'Diyarbakır', 'Erzurum'])
q02 = Question('Where is the capital of United States?',  'Washington DC', ['Washington DC', 'New York',   'Seattle',   'Miami',      'Los Angeles'])
q03 = Question('Where is the capital of United Kingdom?', 'London',        ['London',        'Manchester', 'Oxford',    'Cambridge',  'Liverpool'])
q04 = Question('Where is the capital of Germany?',        'Berlin',        ['Berlin',        'Munih',      'Frankfurt', 'Hamburg',    'Köln'])
q05 = Question('Where is the capital of Belgium?',        'Brussels',      ['Amsterdam',     'Brugge',     'Anvers',    'Arion',      'Halle'])
questionList = [q01, q02, q03, q04, q05]


print(questionList)


import random
import time
# FIGHT GAME


class Character:

    def __init__(self, characterName="Enemy", characterHealth=100, characterPower=5, characterBullet=10):
        self.characterName = characterName
        self.characterHealth = characterHealth
        self.characterPower = characterPower
        self.characterBullet = characterBullet

    def attackerChar(self):
        print(f"The {self.characterName} is attacked..........")
        usingBullet = random.randint(1, 5)
        print(f"The {self.characterName} was attacked for " + str(usingBullet) + " Bullet")
        self.characterBullet -= usingBullet
        return (usingBullet, self.characterPower)

    def defenderChar(self, usingBullet, characterPower):
        print(f"The {self.characterName} is defending..........")
        topDamage = (self.characterPower * usingBullet)
        self.characterHealth -= (self.characterPower * usingBullet)
        print(f"The {self.characterName} has {topDamage} damaged.")

    def overBullet(self):
        if (self.characterBullet <= 0):
            print(f"{self.characterName}'s Bullet is over.")
            if (len(characterList) == 1):
                return
            characterList.remove(self)
            return True
        return False

    def isDead(self):
        if (self.characterHealth <= 0):
            print(f"{self.characterName} is dead.")
            characterList.remove(self)
            return True
        return False

    def winner(self):
        return self.characterName

    def createCharacter(self):
        print(f"""
        Name   : {self.characterName}
        Health : {self.characterHealth}
        Power  : {self.characterPower}
        Bullet : {self.characterBullet}
        """)


characterList = []

char = 0
while char < 10:
    randomName = "Character" + str(char+1)
    randomHealth = random.randint(100, 300)
    randomPower = random.randint(1, 10)
    randomBullet = random.randint(1, 20)

    characterProperties = Character(
        randomName, randomHealth, randomPower, randomBullet)
    characterList.append(characterProperties)

    char += 1

for charList in characterList:
    charList.createCharacter()
    time.sleep(0.25)

# fight = 0

# while (fight < 5):
#     randomCharacterOne = random.randrange(0, 10)
#     randomCharacterTwo = random.randrange(0, 10)

#     returnedValue = characterList[randomCharacterOne].attackerChar()

#     characterList[randomCharacterTwo].defenderChar(returnedValue[0], returnedValue[1])

#     print("Round Over.....")

#     fight += 1

#     time.sleep(0.25)


while (True):
    if (len(characterList) == 10):
        randomCharacterOne = random.randint(0, 9)
        randomCharacterTwo = random.randint(0, 9)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 9)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 9):
        randomCharacterOne = random.randint(0, 8)
        randomCharacterTwo = random.randint(0, 8)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 8)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 8):
        randomCharacterOne = random.randint(0, 7)
        randomCharacterTwo = random.randint(0, 7)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 7)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 7):
        randomCharacterOne = random.randint(0, 6)
        randomCharacterTwo = random.randint(0, 6)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 6)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 6):
        randomCharacterOne = random.randint(0, 5)
        randomCharacterTwo = random.randint(0, 5)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 5)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 5):
        randomCharacterOne = random.randint(0, 4)
        randomCharacterTwo = random.randint(0, 4)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 4)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 4):
        randomCharacterOne = random.randint(0, 3)
        randomCharacterTwo = random.randint(0, 3)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 3)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 3):
        randomCharacterOne = random.randint(0, 2)
        randomCharacterTwo = random.randint(0, 2)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 2)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 2):
        randomCharacterOne = random.randint(0, 1)
        randomCharacterTwo = random.randint(0, 1)
        if (randomCharacterOne == randomCharacterTwo) or (randomCharacterTwo == 0):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterTwo].isDead()
            characterList[randomCharacterOne].overBullet()
            time.sleep(0.5)

            if (len(characterList) == 1):
                winnerOne = characterList[0].winner()
                print("\nMATCH is OVER!")
                print(f"Winner : {winnerOne}")
                input()
                break

    elif (len(characterList) == 1):
        winnerTwo = characterList[0].winner()
        print("\nMATCH is OVER!")
        print(f"Winner: {winnerTwo}")
        input()
        break

    else:
        print("All character is dead. Not winner!")
        input()
        break






ERROR HANDLING I
errorList = ["1", "2", "10", "50", "5a", "10b", "abc"]

for error in errorList:
    try:
        integer = int(error)
        print("Integer Check: ",integer)
    except ValueError:
        continue



# ERROR HANDLING II
while True:
    value = input("Number: ")
    if value == "q":
        break
    try:
        integer = float(value)
        print("Integer Check: ",integer)
    except ValueError:
        print("Invalid Value")
        continue



# ERROR HANDLING III
turkishLetters = "ığüİşçö"
while True:
    dataPass = ""
    password = input("Password: ")

    for p in password:
        if p in turkishLetters:
            raise TypeError("No Turkish Letter Son of a Bitch")
        else:
            pass
        


def checkPassword(password):
    import re
    if len(password) < 8:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", password):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", password):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", password):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]", password):
        raise Exception("Parola değişik karakter içermelidir.")
    elif re.search("\s", password):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Helal len orospu çocuğu")

password = "12345678aVB _"

try:
    checkPassword(password)
except Exception as ex:
    print(ex)
else:
    print("Aferin oç")
finally:
    print("Validation OK")






class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("FAZLA KARAKTER")
        else:
            self.name = name

p = Person("Alperennnnnnnnnnn", 1990)





# OPEN DOCS

with open("newfile.txt", "r", encoding="UTF-8") as file:
# a = 0
# while a < 20:
#     file.write("\nAnanın AMI")
#     a+=1

# for i in file:
#     print(i, end="")

    content = file.read()
    print(content)





# STUDENT REGISTER PROGRAMS

def addStudent():
    nameSurname = input("Student Name & Surname: ")
    studentExam1 = input("Exam1: ")
    studentExam2 = input("Exam2: ")
    studentFinal = input("Final: ")
    with open("studentBase.txt", "a", encoding="UTF-8") as file:
        file.write(nameSurname + " : " + studentExam1 + " , " + studentExam2 + " , " + studentFinal + "\n")


def gradeLetter(equated):
    if 100 >= equated >= 90:
        letterGrade = "AA"
    elif 89 >= equated >= 85:
        letterGrade = "BA"
    elif 84 >= equated >= 80:
        letterGrade = "BB"
    elif 79 >= equated >= 75:
        letterGrade = "CB"
    elif 74 >= equated >= 70:
        letterGrade = "CC"
    elif 69 >= equated >= 65:
        letterGrade = "DC"
    elif 64 >= equated >= 60:
        letterGrade = "DD"
    elif 59 >= equated >= 50:
        letterGrade = "FD"
    elif 49 >= equated >= 0:
        letterGrade = "FF"
    else:
        letterGrade = print("Ananı skm")
    return letterGrade


def gradeCalculator(line):
    line = line[:-1]
    gradeList = line.split(':')

    studentName = gradeList[0]
    studentGrade = gradeList[1]

    studentGrade = studentGrade.split(',')

    gradeOne = int(studentGrade[0])
    gradeTwo = int(studentGrade[1])
    gradeThr = int(studentGrade[2])

    equated = ((gradeOne*0.25) + (gradeTwo*0.25) + (gradeThr*0.5))

    result = "Name & Surname: " + studentName + "\nStudent Grade: " + str(equated) + "\nLetter Grade: " + str(gradeLetter(equated)) + "\n"

    return result


def readStudent():
    with open("studentBase.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(gradeCalculator(line))


def saveResult():
    with open("studentBase.txt", "r", encoding="UTF-8") as file:
        gradeList = []

        for list in file:
            gradeList.append(gradeCalculator(list))
        
        with open("gradeResult.txt", "w", encoding="UTF-8") as fileTwo:
            for list in gradeList:
                fileTwo.write(list + "\n")


while True:
    print("""
    WELCOME TO STUDENT MANAGEMENT PROGRAMS
         1- ADD GRADE
         2- READ GRADE
         3- SAVE RESULT
         Q- EXIT PROGRAM
    """)
    choice = input("Choose: ")

    if choice == "1":
        addStudent()
    elif choice == "2":
        readStudent()
    elif choice == "3":
        saveResult()
    elif choice.upper() == "Q":
        break
    else:
        print("Wrong choice!")
