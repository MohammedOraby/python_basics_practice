## calculate how many times every product was sold
products = ["cake","chips","snacks","milk","cake","milk","milk","chips","milk"]
purchases = {}

for product in products :
    purchases[product] = purchases.get(product,0)+1
print (f"{purchases}")

for k in purchases :
    if purchases[k] == products.count(k):
        print(f"count of {k} is True")
    else :
        print(f"Error counting {k}")
