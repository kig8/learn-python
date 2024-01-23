def main():
    string = input("input: ")
    word_end = shorten(string)
    print(f"print: {word_end}", end = "") 

def shorten(string):

    cut = ["a","e","i","o","u"]

    word = ""
    for i in string:
        if i.lower() not in cut:
            word += i
    return word
if __name__ == "__main__":
    main()