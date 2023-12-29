import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# 10.
# 101.
# 48.
# 0.


def validate(ip):
    if re.search(
        r"^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|2[0-5][0-5])\.){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|2[0-5][0-5])$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
