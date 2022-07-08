#1
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

prod = num1 * num2
if prod > 1000:
    print(num1+num2)
else:
    print(prod)

#2
temp = 0
num = 0
for i in range(1, 10):
    temp = num
    num = i
    print(temp + num)
#3
s = "technoblade"
for char in s:
    if s.index(char) % 2 == 0:
        print(f"index[ {s.index(char)} ] = {char}")
#4
def removeChars(s, num):
    return s[num:]
print(removeChars("Skoppy", 2))
#5
lst = [1, 2, 4 , 1]
if lst[0] == lst[-1]:
    print("True")
#6
lst2 = [1, 3, 7, 5, 10, 3, 8, 15, 13]
for number in lst2:
    if number%5 == 0:
        print(number)
#7
emma_str = "Emma is good developer. Emma is a writer"
count = emma_str.count("Emma")
print(count)

#8
for i in range(1, 6):
    print(str(i)*i)

#9
sampleNum = 100
revNum =  int(str(121)[::-1])
if sampleNum == revNum:
    print("It is same as its reversed self")
else:
    print("It is not the same as its reversed self")
#10
