s = input()

s_lst = list(s)

alnum = False
isalph = False
isdig = False
islow = False
isup = False

for i in s_lst:
    if i.isalnum():
        alnum = True
    if i.isalpha():
        isalph = True

    if i.isdigit():
        isdig = True

    if i.islower():
        islow = True

    if i.isupper():
        isup = True
print(alnum)
print(isalph)
print(isdig)
print(islow)
print(isup)
