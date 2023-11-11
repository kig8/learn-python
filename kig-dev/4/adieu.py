import inflect

p = inflect.engine()
name_list = []


while True:
    try:
        name = input("Name: ")
    except EOFError:
        break

    name_list.append(name)

print("Adieu, adieu, to", p.join(name_list, final_sep=""))
