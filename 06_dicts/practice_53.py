## membership and conditionals in dics --> in/not in operators

students = {"ahmed":88,"mohamed":98,"sara":99}
x = input("enter a key ; ") 
if x in students :
    print (f"student {x} gets {students[x]}%")
else :
    print (f"{x} not in students !")