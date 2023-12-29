import re


def main():
    print(parse(input("HTML: ")))


# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0


def parse(s):
    pattern = r'https?://(www\.)?youtube\.com/embed/(.+?)(?=")'
    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group(2)}"


if __name__ == "__main__":
    main()
