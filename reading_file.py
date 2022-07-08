from sys import argv
script, filename = argv

txt = open(filename)
print(f"The file is {filename}")
print(txt.read())
print("type ur file again:")
file2 = input(">")
txt2 = open(file2)
print(txt2.read())