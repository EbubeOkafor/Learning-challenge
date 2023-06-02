def main():
    plate = input("Plate: ")
    if is_valid(plate) == True :
        print("Valid") 
    else:
        print("Invalid")

def is_valid(s):
    if alpha(s) == True:
        if length(s) == True:
            if digit(s) == True:
                if punct(s) == True:
                    return True
    else:
        return False

def alpha(s):
    if s[:2].isalpha == True:
        return True
    else:
        return False

def length(s):
    if len(s) >=2 and len(s) <= 6:
        return True
    else:
        return False
def digit(s):
    for i in s:
        if i.isdigit() and not s[:7]: #i.endswith(('1','2','3','4','5','6','7','8','9','0')):
            return False
        else:
            return True
def punct(s):
    for i in s:
        if not i == [" ", ".", "!", "?", ";", ":", ","]:
            return True
        else:
            return False
main()