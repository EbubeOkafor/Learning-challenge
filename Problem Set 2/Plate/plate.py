def main():
    plate = input("Plate: ")
    if is_valid(plate) == True :
        print("Valid") 
    else:
        print("Invalid")

def is_valid(s):
    if punct(s):
        return True

    for i in s:
            if i.isdigit() and i == "0":
                return False
            elif i.isdigit() and s[-1].isdigit():
                return True
            elif not i.isdigit:
                return True

    if alpha(s) == True:
        if length(s) == True: #and punct(s) == True:
            return True
    else:
        return False
    
    

def alpha(s):
    if s[0:2].isalpha == True:
        return True
    else:
        return False

def length(s):
    if len(s) >=2 and len(s) <= 6:
        return True
    else:
        return False

def punct(s):
    punctuation = [' ', ',', '!', '.', ':', ';','?']
    for i in s:
        if i in punctuation:
            return True
        elif i in punctuation:
            print("hj")
            return False
        else:
            return True
    

main()