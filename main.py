file = open("text.txt", "rt", encoding = "utf-8")
line = file.readlines()
i = 0
for string in line:
    i += 1
    print(f"Кількість слів у рядку {i}: " + str(len(string.split())))
    length = 0
    for symbol in string:
        if symbol != ' ':
            length += 1
    print(f"Кількість символів у рядку {i}: " + str(length))