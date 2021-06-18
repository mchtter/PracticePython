while True:
    value = input("Number: ")
    if value == "quit":
        break
    try:
        integer = float(value)
        print("Integer Check: ", integer)
    except ValueError:
        print("Invalid Value")
        continue
