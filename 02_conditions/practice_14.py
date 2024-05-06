grade = int (input ("enter your grade : "))

if grade < 0 or grade >100 :
    print ("invalid grafe !!")
elif grade >= 90 and grade <= 100 :
    print ("you got A ")
elif grade >= 80 :
    print ("you got B")
elif grade >= 70 :
    print ("you got C ")
elif grade >60 : 
    print ("you got D")
else :
    print ("you got F")