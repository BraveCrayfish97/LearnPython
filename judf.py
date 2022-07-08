arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

arr1 = [[0, 1, 3, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

#hourglass
for r in range(4):
    s = ""
    e = ""
    even = False
    odd = False
    for i in range(4):
        if r % 2 == 0:
            even = True
            odd = False
            s = s + str(arr[r][i])  + str(arr[r][i+1]) + str(arr[r][i+2]) + "|"
        

        if r % 2 != 0:
            odd = True
            even = False
            e = e + " " + str(arr[r][i+1]) + "  "
            
    if even == True:
        print(s)
    if odd == True:
        print(e)
    
