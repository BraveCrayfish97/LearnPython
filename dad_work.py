not_num = True
while(not_num):
    try:

        first_n = int(input("Type a number and I will give you the sum of the first ___ numbers\n> "))
        sum_1 = int(first_n*(first_n + 1)/2)
        print(f"The sum of the first {first_n} numbers is {sum_1}")
        not_num = False
    except ValueError:
        print("Please type a number")


not_good = True
while(not_good):
    try:

        n = int(input("Type a number and I will give you the sum of the first ___ numbers squared. Ex: 1^2 + 2^2 + 3^2\n> "))
        sum_2 = n*(n + 1)*(2*n + 1)/6
        print(f"The sum of the first {n} numbers squared is {sum_2}")
        not_good = False

    except ValueError:
        print("Please type a number")
    
#james go to google and then press control i , got it?

no_bien = True
while(no_bien):
    try:
        not_prime = False
        prime = int(input("Type a number and I will tell you if its prime or not\n> "))
        for x in range(2, round(prime/2)):
            if prime % x == 0:
                print("Your number is not prime")
                not_prime = True

        if not_prime == False:
            print("Your number is prime")        
        no_bien = False

    except ValueError:
        print("Please type a number")

bad = True
while(bad):
    try:
        number = int(input("Type a number and I will tell you how many digits it has\n> "))
        print("Your number has", len(str(number)), "digits.")
        bad = False
    except ValueError:
        print("Please type a number")


mal = True
#while(mal):
    #try:
     #   numero = input("Type a number and I will tell you how many digits it has\n> ")
      #  
       # print(bot)
        #reverse = 
        #print(f"Your number reversed is {reverse}")
        #mal = False
    #except ValueError:
    #    print("Please type a number")