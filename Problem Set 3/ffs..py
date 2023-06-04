text = input()

for i in text:
    if i.isdigit() == True:
        i = i.replace(i, "/")
        text = i.split("/")
        break

print(text[1])