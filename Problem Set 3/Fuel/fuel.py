while True:
    try:
        fraction = input("Enter a fraction: ")
        x, y = map(int, fraction.split("/"))
        percentage = round((x/y)*100)
        if x > y:
            print("Numerator cannot be greater than denominator")
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        break
if percentage <= 1:
    print(f"E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")