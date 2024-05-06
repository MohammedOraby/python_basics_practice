mixed_list = [1,2,2,3,4,"a","b","a"]

# unique_list = []

# for item in mixed_list :
#     if item not in unique_list :
#         unique_list.append(item)
# print (unique_list)

unique_list = list(set(mixed_list))
print (unique_list)