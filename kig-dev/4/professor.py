import random


def main():
    level = get_level()
    score = 0

    for _ in range(4):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y

        n = 0
        while n < 3:
            try:
                result = int(input(f"{x} + {y} = "))
                if sum != result:
                    raise ValueError
            except ValueError:
                n += 1
                print("EEE")
            else:
                score += 1
                break

        # if n == 3:
        #     break

    print(f"Score: {score}")


def get_level():
    levels = (1, 2, 3)

    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

        if n in levels:
            return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
