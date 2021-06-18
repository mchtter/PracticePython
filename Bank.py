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
