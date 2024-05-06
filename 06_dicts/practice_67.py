## sum of income 
income = {"job":2000,"online":1000,"investment":3000}
total_income = 0
for value in income.values():
    total_income += value
print (f"total income : {total_income}")