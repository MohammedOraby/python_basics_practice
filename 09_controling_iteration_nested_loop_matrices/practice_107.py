a = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# for i in range(4):
#     for j in range(4):
#         if i == j:
#             a[i][j] = 1

for x in range(4):
    a[x][x] = 1    

for row in a:
    print(row)