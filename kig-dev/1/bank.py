greeting = input("Greeting: ").strip()
is_start_with_h = greeting.startswith("H")
is_start_with_hello = greeting.startswith("Hello")

print(is_start_with_h, is_start_with_hello, sep=" | ")

if is_start_with_hello:
    print("$0")
elif is_start_with_h:
    print("$20")
else:
    print("$100")
