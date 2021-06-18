errorList = ["1", "2", "10", "50", "5a", "10b", "abc"]

for error in errorList:
    try:
        integer = int(error)
        print("Integer Check: ", integer)
    except ValueError:
        continue
