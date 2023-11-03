def main():
    result = get_fraction("Fraction: ")
    print(fuel_load(result))


def get_fraction(text):
    while True:
        x, y = input(text).split("/")

        if x > y:
            continue

        try:
            x, y = int(x), int(y)
            fraction = round((x / y) * 100)
            break
        except (ValueError, ZeroDivisionError):
            pass

    return fraction


def fuel_load(fraction):
    load = str(fraction) + "%"

    if fraction > 99:
        load = "F"
    elif fraction < 1:
        load = "E"

    return load


main()
