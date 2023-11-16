def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return all(
        [
            not_allowed_chars(s),
            is_length(s),
            is_start_two_letter(s),
            is_num_used_correctly(s),
        ]
    )


def is_start_two_letter(s):
    return s[:2].isalpha()


def is_length(s, min=2, max=6):
    return min <= len(s) <= max


def is_num_used_correctly(s):
    examined_list = s[2:]

    if s.isalpha():
        return True
    else:
        for i in range(len(examined_list)):
            if examined_list[i].isdigit():
                if examined_list[i] != "0" and examined_list[i:].isdigit():
                    return True
                else:
                    return False


def not_allowed_chars(s):
    punctuation_chars = ",-_.:; "

    for char in s:
        if char in punctuation_chars:
            return False
    return True


if __name__ == "__main__":
    main()
