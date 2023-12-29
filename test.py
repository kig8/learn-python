a_list = [1, 2, 3, 4, 5, 6]

b = map(lambda x: x if x > 2 else x + 2, a_list)
print([*b])

# print(arr_2, arr_3)
