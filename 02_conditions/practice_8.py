test_age = 18
age = int(input("enter your age : "))
if age >= test_age : 
    print ("you can apply for a drivjng test :)")  
else :
    print (f"you are not eligible apply for a drivjng test \n you can apply after {test_age-age} yrs")