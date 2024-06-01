## create notes app

print("Enter a note or done to close")
notes = []
while True:
    note = input("Enter an note : ")
    if note == "done".lower():
       break
    notes.append(note)
with open("notes.txt","a") as file:
    for note in notes:
        file.write(note + "\n")