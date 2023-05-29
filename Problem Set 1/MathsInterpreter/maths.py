maths = input("Enter a basic arithmetic expression: ")
maths = maths.split()
if maths[1] == "/":
    maths[0] = int(maths[0])
    maths[2] = int(maths[2])
    expression = maths[0] / maths[2]
    print(round(expression, 1))
elif maths[1] == "-":
    maths[0] = int(maths[0])
    maths[2] = int(maths[2])
    expression = maths[0] - maths[2]
    print(f"{expression, .1f}")
elif maths[1] == "+":
    maths[0] = int(maths[0])
    maths[2] = int(maths[2])
    expression = maths[0] + maths[2]
    print(round(expression, 1))
elif maths[1] == "*":
    maths[0] = int(maths[0])
    maths[2] = int(maths[2])
    expression = maths[0] * maths[2]
    print(round(expression, 1))
elif maths[1] == "%":
    maths[0] = int(maths[0])
    maths[2] = int(maths[2])
    expression = maths[0] % maths[2]
    print(round(expression, 1))
else:
    print("invalid arithmetic operation!")
