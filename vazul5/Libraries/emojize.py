# import requests
import emoji
# requests.get("https://raw.githubusercontent.com/carpedm20/emoji/master/emoji/unicode_codes/data_dict.py")

e = input("Input: ")
f = emoji.emojize(e, language='alias')
print(f)



