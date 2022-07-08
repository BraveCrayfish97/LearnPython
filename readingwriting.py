from sys import argv
script, filename = argv
print(f"we r going to erase{filename}")
print("Opening file...")
target = open(filename, 'w')

print("Deleting the content in the file")
target.truncate()

print("Now type 3 diiferent lines")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Now I will write those botty lines into the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Now we will close the file")
target.close()