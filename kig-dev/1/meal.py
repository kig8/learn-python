konak_valtozo = 0


def main():
    time = input("What time is it? ")
    res_time = convert(time)

    if 7 <= res_time <= 8:
        print("breakfast time")
    elif 12 <= res_time <= 13:
        print("lunch time")
    elif 18 <= res_time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    dec_time = float(hour) + (1 / (60 / float(minute)))

    return dec_time


if __name__ == "__main__":
    main()
