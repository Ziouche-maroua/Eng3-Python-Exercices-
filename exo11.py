def print_hash_line():
    
    
    width = int(input("Width: "))
    if width > 0:
        print("#" * width)
    else:
        print("Please enter a positive integer.")
    

# Print a line of hash characters
print_hash_line()
