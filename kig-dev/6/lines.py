import sys


def main():
    loc = check_args(sys.argv)
    print(loc)


def check_args(args):
    args_len = len(args)

    if args_len < 2:
        sys.exit("Too few command-line arguments")
    elif args_len > 2:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        try:
            return count_loc(args[1])
        except FileNotFoundError:
            sys.exit("File does not exist")


def count_loc(file_name):
    countable_line = 0

    with open(file_name) as file:
        for line in file:
            if line.strip() and not line.strip().startswith("#"):
                countable_line += 1

            continue

    return countable_line


if __name__ == "__main__":
    main()
