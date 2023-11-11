import random
import sys


def main():
    level = prompt_integer("Level: ")
    random_int = random.randint(1, level)
    print_result(random_int)


def prompt_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            continue

        if n > 0:
            break

    return n


def print_result(int):
    while True:
        guess = prompt_integer("Guess: ")

        if int > guess:
            print("Too small!")
        elif int < guess:
            print("Too large")
        else:
            sys.exit("Just right!")


if __name__ == "__main__":
    main()
