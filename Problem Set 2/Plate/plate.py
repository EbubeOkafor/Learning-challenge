def main():
    plate = input("Plate: ")
    if is_valid(plate) == True :
        print("Valid") 
    else:
        print("Invalid")

def is_valid(s):
    for i in s:
            if i.isdigit() and i == "0":
                return False
            elif i.isdigit() and s[-1].isdigit():
                return True
            elif not i.isdigit:
                return True
                
    if alpha(s) == True:
        if length(s) == True:
              return True
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

#def digit(s):
 #   for i in s:
  #      if i.isdigit():
   #         m = re.search(r'\d+$', s)
    #        if m == True:
     #           return True
        
    
def punct(s):
    punctuation = [' ', ',', '!', '.', ':', ';','?']
    for i in s:
        if i in punctuation:
            return False
        elif not i in punctuation:
            return True
        else:
            return True

main()