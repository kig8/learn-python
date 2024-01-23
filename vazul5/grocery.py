# d = {}
# whele True:
#     try:
#        item = input("")
#     except EOFError:
#         break

#     if item in d:
#         d[item]+= 1

#     else:
#         d[item]= 1
item_dict = {}

while True:
    try:
        item = input("").strip().lower()
    except EOFError:
        break

    if item in item_dict:
        item_dict[item] += 1
    else:
        item_dict[item] = 1

for item, count in item_dict.items():
    print(f"{count} {item.upper()} ")
# TUDO ábcé sorend!!!!!
