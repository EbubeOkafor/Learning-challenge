menu = {

    "Baja Taco": 4.00,

    "Burrito": 7.50,

    "Bowl": 8.50,

    "Nachos": 11.00,

    "Quesadilla": 8.50,

    "Super Burrito": 8.50,

    "Super Quesadilla": 9.50,

    "Taco": 3.00,

    "Tortilla Salad": 8.00

}

order_total = 0.0

while True:

    try:

        item = input("Enter an item from the menu (or press Ctrl-D to finish): ")

        # Exit the loop if the user inputs control-d (EOF)

        if not item:

            break

        # Convert the input to title case and check if it exists in the menu

        item = item.title()

        if item not in menu:

            print("Invalid item. Please choose an item from the menu.")

            continue

        # Add the item price to the order total

        order_total += menu[item]

        # Display the updated total cost

        print("Total cost:", "${:.2f}".format(order_total))

    except Exception as e:

        print("An error occurred:", str(e))
