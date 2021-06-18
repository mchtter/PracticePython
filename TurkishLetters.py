turkishLetters = "ığüİşçö"
while True:
    dataPass = ""
    password = input("Password: ")

    for p in password:
        if p in turkishLetters:
            raise TypeError("No Turkish Letter Son of a Bitch")
        else:
            pass
