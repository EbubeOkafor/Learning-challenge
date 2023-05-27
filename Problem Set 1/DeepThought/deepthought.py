question = input("What is the Answer to the Great Question of life? ")
question = question.lower()
if question == "foury-two" or "fourty two":
    print("Yes")
elif int(question) == 42:
    print("Yes")
else:
    print("No")

