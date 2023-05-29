
def main():

    mealtime = input("What is the time?")

    mealtime = convert(mealtime)

    if mealtime >= 7.0 and mealtime <= 8.0:

        print("Breakfast Time!")

    elif mealtime >= 12.0 and mealtime <= 13.0:

        print("Lunch Time!")

    elif mealtime >= 18.0 and mealtime <= 19.0:

        print("Dinner Time!")

def convert(time):

    time = time.split(':')

    time[0] = float(time[0])

    time[1] = float(time[1])

    floatTime = (time[0]*60) + time[1]

    floatTime = floatTime / 60

    return round(floatTime, 1)

if __name__ == "__main__":

        main()
   
    











