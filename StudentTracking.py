def addStudent():
    nameSurname = input("Student Name & Surname: ")
    studentExam1 = input("Exam1: ")
    studentExam2 = input("Exam2: ")
    studentFinal = input("Final: ")
    with open("studentBase.txt", "a", encoding="UTF-8") as file:
        file.write(nameSurname + " : " + studentExam1 + " , " +
                   studentExam2 + " , " + studentFinal + "\n")


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

    result = "Name & Surname: " + studentName + "\nStudent Grade: " + \
        str(equated) + "\nLetter Grade: " + str(gradeLetter(equated)) + "\n"

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
