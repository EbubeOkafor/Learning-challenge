greeting = input("Enter a greeting: ")
greeting = greeting.lower()
if "hello" in greeting:
    print("$0")
elif "h" in greeting and "hello" not in greeting:
    print("$20")
else:
    print("$100")
