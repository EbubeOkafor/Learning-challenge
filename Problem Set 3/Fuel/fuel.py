while True:
    try:
        fraction = input("Enter a fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        percent = (x/y)*100
    except  ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        break
if x > y:
    raise ValueError("x should be less than y")
else:
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(percent)
    