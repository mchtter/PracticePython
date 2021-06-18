
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
        print("Bütün şartlar sağlandı.")


password = "12345678aVB _"

try:
    checkPassword(password)
except Exception as ex:
    print(ex)
else:
    print("Aferin")
finally:
    print("Validation OK")


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("FAZLA KARAKTER")
        else:
            self.name = name


p = Person("Alperennnnnnnnnnn", 1990)
