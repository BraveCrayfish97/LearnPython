original_file = input("What file?")
txt = open(original_file)
content = txt.read()
num_lst = content.split('\n')
print(num_lst)

ordered_lst = []
for num in num_lst:
    num = int(num)
    print(num)
    ordered_lst.append(num)
writefile = open("dad_ordered.txt", 'w')

ordered_lst.sort()
print(ordered_lst)
for ordered_num in ordered_lst:
    writefile.write(str(ordered_num))
    writefile.write("\n")