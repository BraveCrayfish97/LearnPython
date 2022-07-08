on = True
def add(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while (on):
    #while(True):
    valid_inp = True
    try:

        f = open('calc_input.txt', 'r')
        num1 = int(f.readline())
        num2 = int(f.readline())
            #num1 = int(input("Enter number: "))
            #num2 = int(input("Enter number: "))
        if num2 == 0:
            print("Don't set the 2nd number as 0 pls")
            continue
        break
    except:
        print("Please enter a number")
    if valid_inp:
        a = add(num1, num2)
        s = minus(num1, num2)
        m = multiply(num1, num2)
        d = divide(num1, num2)
        print(f"{num1}+{num2} = {a}")
        print(f"{num1}-{num2} = {s}")
        print(f"{num1}*{num2} = {m}")
        print(f"{num1}/{num2} = {d}")
        yes_no = True
        while (yes_no):
            inp = input("Do you want to keep going?\n>")
            
            if inp == "yes":
                break
            elif inp == "no":
                on = False
                break
            else:
                print("Please enter 'yes' or 'no'")

