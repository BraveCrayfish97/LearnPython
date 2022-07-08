def timeConversion(s):
    #
    # Write your code here.
    #
    #military time
    string = ""
    char_lst = list(s)
    if char_lst[-2] + char_lst[-1] == "PM":
        t_tup = tuple(str(int(char_lst[0] + char_lst[1]) + 12))
        char_lst[0], char_lst[1] = t_tup
        char_lst.remove("P")
        char_lst.remove("M")
    else:
        char_lst.remove("A")
        char_lst.remove("M")

    for item in char_lst:
        string = string + item
    s_lst = list(string)

    if s_lst[0] + s_lst[1] == "24":
        s_lst[0] = "0"
        s_lst[1] = "0"
    
        yeet = ""
        for lol in s_lst:
            yeet = yeet + lol
        return yeet
    else:
        
        return string
n = input()
res = timeConversion(n)
print(res)