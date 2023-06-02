Amount = 50
print("Amount Due: ", Amount)
while Amount > 0:
    coin = int(input("Insert coin: "))
    match coin:
        case 25|10|5:
            if coin > Amount:
                print("Change Owed: ", Amount)
                break
            else:
                Amount = Amount - coin
            if Amount == 0:
                    print("Change Owed: 0")
            else:
                print("Amount Due: ", Amount)
        case _:
            print("Amount Due: ", Amount)