#number of entries in phonebook
n = int(input().strip())
phoneBook = {}

#assign in phoneBook
for i in range(n):
    name, num = input().strip().split(' ')
    phoneBook[name] = num

#query phoneBook while there is input, exit when EOF
while(True):
    try:
        qName = input().strip()
        if qName in phoneBook:
            print('{}={}'.format(qName, phoneBook[qName]))
        else:
            print('Not found')
    except EOFError:
        break