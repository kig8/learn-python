def main():
    prompt_date()


def prompt_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ")
        short_date = date.split("/")
        long_date = date.split()

        # September 8, 1636
        # September 8 1636
        # 8 September 1636
        if long_date[0] in months:
            try:
                m = int(months.index(long_date[0])) + 1
                d = int(long_date[1].strip(","))
                y = int(long_date[2])
            except ValueError:
                pass

        else:
            try:
                m = int(short_date[0])
                d = int(short_date[1])
                y = int(short_date[2])
            except ValueError:
                pass

        if 1 <= d <= 31 and 1 <= m <= 12 and y > 1:
            print(f"{y}-{m:02d}-{d:02d}")
            break
        else:
            continue


main()
