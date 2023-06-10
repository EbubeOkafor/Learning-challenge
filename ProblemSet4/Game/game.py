import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level < 0:
            continue
        else:
            break
num = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < 0:
            continue
        elif guess < num:
            print("Too small!")
            continue
        elif guess > num:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break