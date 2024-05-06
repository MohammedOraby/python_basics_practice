store_1 = {"store name":"the cool store",
           "phone":1234,
           "fruits":["orang","banana","apple"],
           "snacks":["cake","candy",]}

store_2 = {"store name":"the awesome store",
           "phone":567890,
           "fruits":["grapefruit","strawberries"],
           "snacks":["chips","sandwiches",]}

stores = [store_1,store_2]
for store in stores :
    print (store["store name"], store["phone"])
