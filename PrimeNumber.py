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
