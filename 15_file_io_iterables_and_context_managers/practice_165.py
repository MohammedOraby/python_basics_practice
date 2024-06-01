## context managers
# with

with open("universities.txt","w") as uni_file:
    # (with) allow me to operate on the file and close it automatically at the end of the statement
    uni_file.write("MIT\n")
    uni_file.write("oxford\n")
    uni_file.write("stanford\n")
