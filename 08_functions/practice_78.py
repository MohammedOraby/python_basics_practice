products = {"soda":33,"cake":45,"chips":11}

def  products_details (d):
    for product,price in products.items():
        print(f"product : {product} - price : {price}")

products_details(products)


