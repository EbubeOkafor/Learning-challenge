while True:

    try:

        fraction = input("Enter a fraction in the format x/y: ")

        x, y = map(int, fraction.split('/'))

        if x > y or y == 0:

            raise ValueError("Invalid fraction. Numerator cannot be greater than the denominator, and denominator cannot be zero.")

        percentage = (x / y) * 100

        rounded_percentage = round(percentage)

        if rounded_percentage <= 1:

            grade = 'E'

        elif rounded_percentage >= 99:

            grade = 'F'

        else:

            grade = str(rounded_percentage) + '%'

        print("Grade:", grade)

        break  # Exit the loop if the fraction is valid

    except ValueError as e:

        print("Invalid fraction input:", str(e))

    except Exception as e:

        print("An error occurred:", str(e))
