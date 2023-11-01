def main():
    input_name = input("camelCase: ")
    print("snake_case: " + get_snake_name(input_name))


def get_snake_name(name):
    snake_name = ""

    for letter in name:
        if letter.isupper():
            snake_name += "_" + letter.lower()
        else:
            snake_name += letter

    return snake_name


main()
