import random
results = []
while True:
    level = int(input("Level: "))
    t = [1, 2, 3]
    if level not in t:
        continue
    else:
        break
i = 0
while i < 10:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = x + y
    j = 0
    while j < 3:
        result = int(input(f"{x} + {y} = "))
        if result == z:
            results.append(result)
            i += 1
            break
            continue
        else:
            print("EEE")
            j += 1
            if j < 3:
                continue
            else:
                print(z)
                i += 1
                continue
l = len(results)
print(f"Score: {l}")

