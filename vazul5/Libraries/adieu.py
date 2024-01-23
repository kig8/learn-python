names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
else:
    last_name = names.pop()
    names_str = ", ".join(names)
    fin = f"Adieu, adieu, to {names_str}, and {last_name}"
    print(fin)