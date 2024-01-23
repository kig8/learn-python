import re
import sys


def main():
    print(convert(input("Hours: ")))


# 9:00 AM to 5:00 PM
# 9 AM to 5 PM


def convert(s):
    pattern = r"[1-2]?[0-9]:[0-5][0-9]"
    if matches := re.search(pattern, s):
        # Check the correct ante meridiem (AM) and post meridiem (PM) format
        return matches[0]


if __name__ == "__main__":
    main()
