names_file = open("file.txt")

for name in names_file:
    print(name.strip())

names_file.close()