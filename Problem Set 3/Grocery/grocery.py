from collections import defaultdict

grocery_list = defaultdict(int)

while True:

    try:

        item = input("Enter an item for your grocery list (or press Ctrl-D to finish): ")

        # Exit the loop if the user inputs control-d (EOF)
    except Exception as e:

        print("An error occurred:", str(e))

        if not item:

            break

        # Convert the input to uppercase and count the item occurrences

item = item.upper()

grocery_list[item] += 1

    
# Sort the grocery list items alphabetically

sorted_list = sorted(grocery_list.items(), key=lambda x: x[0])

# Display the grocery list with item counts

for item, count in sorted_list:

    print(f"{count} {item}")
