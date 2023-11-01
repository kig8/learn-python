def main():
    result_string = convert(input())
    print(result_string)


def convert(s):
    new_string = str(s).replace(":)", "🙂").replace(":(", "☹️")
    return new_string


main()
