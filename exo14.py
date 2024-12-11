def print_framed_string():
    # Request input from the user
    user_string = input("Please enter a string: ").strip()
    frame_width = 30

    # Handle strings longer than the frame width
    if len(user_string) > frame_width - 2:
        print("Error: The string is too long to fit inside the frame.")
        return

    # Calculate padding
    padding = frame_width - len(user_string)
    left_padding = padding // 2
    right_padding = padding - left_padding

    # Print the frame
    print("*" * frame_width)
    print("*" + " " * (frame_width - 2) + "*")
    print("*" + " " * left_padding + user_string + " " * right_padding + "*")
    print("*" + " " * (frame_width - 2) + "*")
    print("*" * frame_width)

print_framed_string()