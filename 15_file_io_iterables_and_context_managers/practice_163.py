## open a file doesn't exists will create this file
hobbies_file = open("hobbies.txt","w")
## open a file in "w" (write mode) delete the file content

# write in a file 
hobbies_file.write("reading\n")
hobbies_file.write("sports\n")
hobbies_file.write("computer games\n")

hobbies_file.close()