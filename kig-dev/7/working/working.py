import re
import sys


def main():
    print(convert(input("Hours: ")))


# 9:00 AM to 5:00 PM
# 9 AM to 5 PM


def convert(s):
    pattern = r"\d+"
    if matches := re.findall(pattern, s):
        return matches


if __name__ == "__main__":
    main()
