## get() method

purchases = {"cake":3,"chips":4,"candy":6}
item = input ("enter an item to buy : ")


# if item in purchases :
#     purchases[item]+=1
# else :
#     purchases[item] = 1

purchases[item] = purchases.get(item,0)+1
print (purchases)