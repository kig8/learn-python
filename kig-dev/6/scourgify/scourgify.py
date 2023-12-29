import csv
import sys


def main():
    args = sys.argv
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not args[1].endswith(".csv") or not args[2].endswith(".csv"):
            sys.exit("Not a python file")
        else:
            try:
                table = read_data(args[1])
            except FileNotFoundError:
                sys.exit("File does not exist")

    write_data(table, new_file=args[2])


def read_data(file_name):
    students = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for item in reader:
            students.append(item)

    return students


def write_data(data, new_file):
    with open(new_file, "w", newline="") as file:
        writer = csv.DictWriter(file, ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(
            [
                {
                    "last": row["name"].split(",")[0],
                    "first": row["name"].split(", ")[1],
                    "house": row["house"],
                }
                for row in data
            ]
        )


if __name__ == "__main__":
    main()
