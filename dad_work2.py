file_name = input("What file do u want to copy from?")
content = open(file_name)
data = content.read()
print("Copying data to otherwords.txt ...")
to_file = "new.txt"
to_file_content = open(to_file, 'a')
to_file_content.write("\n")
to_file_content.write(data)

to_file_content.close()
content.close()
