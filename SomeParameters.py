someParameters = input("Please Enter some parameters: ")


def createList(*someParameters):
    paramList = []

    for add in someParameters:
        paramList.append(add)
    print(paramList)
    return paramList


createList(someParameters)
