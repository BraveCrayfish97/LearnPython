bot = True
lst = []
while bot:
    x = input("Enter num -> ")
    s = True
    lst.append(x)
    while s:
        try:
            y_n = input("Do you want to keep going")
            if y_n == "yes" or y_n == "Yes":
                brk = False
                break
            elif y_n == "no" or y_n == "No":
                brk = True
                break
            else:
                pass
                
        except:
            print("Type 'Yes' or 'no'\n")
            
    
    if brk == True:
        break
print("The biggest number is " + str(max(lst)))
print("The smallest number is " + str(min(lst)))
