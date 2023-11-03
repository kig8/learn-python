import emoji

input_str = input("Input: ")
result = emoji.emojize(input_str, language="alias")

print("Output: ", result)
