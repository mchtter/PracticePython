with open("newfile.txt", "r", encoding="UTF-8") as file:
    a = 0
    while a < 20:
        file.write("\nHello World!")
        a += 1

    for i in file:
        print(i, end="")

    content = file.read()
    print(content)
