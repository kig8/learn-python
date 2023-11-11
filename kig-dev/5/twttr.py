def main():
    input_w = input("Input: ")
    print("Output:", shorten(input_w))


def shorten(word):
    vowels = ["a", "e", "u", "i", "o"]
    result = ""

    for l in word:
        if l.lower() not in vowels:
            result += l

    return result


if __name__ == "__main__":
    main()
