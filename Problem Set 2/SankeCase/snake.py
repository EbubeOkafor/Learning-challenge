def main():
    string = input("camelCase: ")
    convert_case(string)

def convert_case(case):
    for i in case:
        if i.isupper() == True:
            case = case.replace(i, "_" + i.lower())
    print("snake_case: ", case)

main()