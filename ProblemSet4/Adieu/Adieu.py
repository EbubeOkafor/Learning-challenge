names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

count = len(names)
if count == 1:
    print(f"Adieu, adieu, to {name}")
elif count == 2:
    print(f"Adie, adieu, to {name[0]} and {name[1]}")
else:
    farewell = ", ".join(names[:-1]) + f", and {names[-1]}"
    print(f"Adieu, adieu, to {farewell}")