inputNumber = int(input("Please enter number for divisor calculation: "))


def checkFactor(number):
    factorList = []

    for factor in range(2, number):
        if number % factor == 0:
            factorList.append(factor)
    print(factorList)
    return factorList


checkFactor(inputNumber)
