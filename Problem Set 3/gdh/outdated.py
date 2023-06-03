months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Enter a date in month-day-year format (e.g., 9/8/1636 or September 8, 1636): ")

        # Check if the date is in month-day-year format
        if "/" in date:
            month, day, year = map(int, date.split('/'))
        else:
            month_str, day_str, year_str = date.split()
            month = months.index(month_str) + 1
            day = int(day_str)
            year = int(year_str)

        # Validate the date
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            raise ValueError("Invalid date.")

        # Format the date in ISO 8601 format
        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"

        print("Formatted date:", formatted_date)
        break  # Exit the loop if the date is valid
    except ValueError as e:
        print("Invalid date input:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
