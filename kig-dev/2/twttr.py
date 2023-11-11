input_v = input("Input: ")
vowels = ["a", "e", "u", "i", "o"]

# print("".join([l for l in input_v if l not in vowels])) --> List comprehension
print("Output: ", end="")

for l in input_v:
    if l.lower() not in vowels:
        print(l, end="")

print()
