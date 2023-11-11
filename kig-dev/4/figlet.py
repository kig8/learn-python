import sys
import pyfiglet
import random

figlet = pyfiglet.Figlet()
font_list = figlet.getFonts()
font = random.choice(font_list)
f_arg_len = len(sys.argv)

if 1 < f_arg_len < 4:
    # check the first arg
    if sys.argv[1] not in ("-f", "--font"):
        sys.exit("Invalid usage")

    # second arg is the font, if we have
    if f_arg_len == 3:
        if sys.argv[2] not in font_list:
            sys.exit("Invalid usage")
        else:
            font = sys.argv[2]

text = input("Input: ")
result = pyfiglet.figlet_format(text, font)

print(f"Output: \n{result}")

#             0             1               2
# python      figlet.py     -f / --font     (font_name)
