months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

while True:
    try:
        date = input("Enter a date in month-day-year format: ").lower()
        # Check if the date is in month-day-year format
        if "/" in date:
            month, day, year = map(int, date.split('/'))
        else:
            month_str, day_str, year_str = date.split()
            month = months.index(month_str) + 1
            day_str = day_str.replace(",", "")
            day = int(day_str)
            year = int(year_str)
        # Validate the date
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            print("Invalid date!")
            continue

        # Format the date in ISO 8601 format
        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"

        print("Formatted date:", formatted_date)
        break
    except ValueError:
        print("Invalid Value!")