while True:
    copies = int(input("how many copies you want to buy (2 in stock) ? "))
    if copies > 0 and copies <= 2:
        break

print(f"Order successfully: {copies} copies")