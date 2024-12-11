def print_hash_rectangle():
    # Request input from the user

    width = int(input("Width: "))
    height = int(input("Height: "))
    if width > 0 and height > 0:
        for _ in range(height):
            print("#" * width)
    else:
        print("Please enter positive integers for both width and height.")
    



# Print a rectangle of hash characters
print_hash_rectangle()
