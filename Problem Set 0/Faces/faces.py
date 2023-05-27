def convert(word): #user-defined function that takes an argument and perfoms the emoticon to emoji conversion.
    word = word.replace(':)','🙂')
    word = word.replace(':(','🙁')
    print(word)

def main():
    faces = input() #prompts user for input.
    convert(faces)

main()