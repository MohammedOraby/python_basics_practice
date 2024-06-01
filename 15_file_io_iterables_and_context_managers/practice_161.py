## reading a file 
names_file = open("file.txt", "r")

# file_content = names_file.read()

# file_content = names_file.readline()

file_content = names_file.readlines() ## read file in a list

print(file_content)

names_file.close()