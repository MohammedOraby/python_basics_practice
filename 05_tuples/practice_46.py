## extended unpacking 
# x,*y = [1,2,3,5]
# print (x)
# print (y)

############################

# a,*b = (5,6,7,8,9)
# print(a)
# print(b) #always the output in a list

############################# 
## practice membership operators(in,not in) 
emails = [
    "sara@gmail.com",
    "oraby.gmail.com",
    "mohamed2gmail.com"
]
for email in emails :
    if "@" not in email :
        print (f"{email} is invalid")
    