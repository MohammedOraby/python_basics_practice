## tip in meal 
meal_coast = float(input("enter meal coast :"))
tip_percentage = float(input("enter tip percentagr (5% , 10%) : ")) / 100
total = meal_coast + tip_percentage * meal_coast
print (f"total meal coast : {total}")