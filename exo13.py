def underline_strings():
    while True:
        user_input = input("Please type in a string: ").strip()
        if user_input == "":
            break
        print(user_input)
        print("-" * 80)

underline_strings()