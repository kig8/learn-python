from PIL import Image, ImageOps
import sys


def main():
    args = sys.argv
    file_ext = (".jpg", ".jpeg", ".png")

    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not args[1].endswith(file_ext) and not args[2].endswith(file_ext):
            sys.exit("Invalid input")
        else:
            if args[1].rsplit(".", 1)[1] != args[2].rsplit(".", 1)[1]:
                sys.exit("Input and output have different extensions")
            else:
                try:
                    merge_pics(args[1], args[2])
                except FileNotFoundError:
                    sys.exit("File does not exist")


def merge_pics(before, after):
    shirt_pic = Image.open("./shirt.png")
    pic_size = shirt_pic.size

    with Image.open(before) as pic:
        cropped_pic = ImageOps.fit(pic, pic_size)
        cropped_pic.paste(shirt_pic, shirt_pic)
        cropped_pic.save(after)


if __name__ == "__main__":
    main()
