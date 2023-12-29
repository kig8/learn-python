from tabulate import tabulate
import sys
import csv


def main():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not args[1].endswith(".csv"):
            sys.exit("Not a python file")
        else:
            try:
                table = get_data(args[1])
            except FileNotFoundError:
                sys.exit("File does not exist")

    print(table)


def get_data(file_name):
    with open(file_name) as file:
        # it creates an iterator not an iteratable obj
        reader = csv.reader(file)

        # this built-in fn read out the first item
        # after this next() line the iterator omits the first line
        header = next(reader)
        table = [item for item in reader]

    return tabulate(table, header, tablefmt="grid")


if __name__ == "__main__":
    main()
