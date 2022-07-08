if __name__ == '__main__':
    n = int(input())
b_lst = list(bin(n))
b_lst.remove('b')

hi = b_lst.pop([0])
current = b_lst[0]
count = 0
new_b = []
print(b_lst)
for val in b_lst:
    if val == "1":
        if val == current:
            count = count + 1
        else:

            new_b.append(count)
            current = val
            count = 1

    else:
        print("count is 0")
        count = 0
        current = val
        print("This is 0")

new_b.append(count)
print(new_b)