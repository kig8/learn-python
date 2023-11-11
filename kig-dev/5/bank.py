def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


def value(greeting):
    is_start_with_h = greeting.lower().startswith("h")
    is_start_with_hello = greeting.lower().startswith("hello")

    if is_start_with_hello:
        return 0
    elif is_start_with_h:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
