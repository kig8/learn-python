def main():
    get_item()


def get_item():
    items = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            for i in sorted_dict:
                print(items[i], i)
            break

        if item in items:
            items[item] += 1
        else:
            items[item] = 1

        sorted_dict = sorted(list(items))


main()
