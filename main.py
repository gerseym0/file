file = open("text.txt", encoding = "utf-8")
text = file.read()
print("Кількість слів у рядку: " + str(len(text.split())))
len = 0
for с in text:
    if с != ' ':
        len += 1        
print("Кількість символів в рядку: " + str(len))