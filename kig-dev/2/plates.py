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
    i = 0
    result = False

    for l in s[2:]:
        if l.isdigit():
            if i == 0:
                if l == "0" or not s[-1].isdigit():
                    return False
                i += 1
            result = True
        elif not l.isdigit() and i > 0:
            return False

    return result


def not_allowed_chars(s):
    punctuation_chars = ",-_.:; "

    for char in s:
        if char in punctuation_chars:
            return False
    return True


main()
