def list_initialization_and_append():
    # Initialize two empty lists
    numbers = []
    shoe_sizes = []

    # Append items to the numbers list
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    # Append items to the shoe_sizes list using a loop
    for size in [8, 9, 10, 11, 12]:
        shoe_sizes.append(size)

    # Print both lists with descriptive labels
    print(f"Numbers List: {numbers}")
    print(f"Shoe Sizes List: {shoe_sizes}")

    # Bonus: 
    # Handle duplicates in numbers
    numbers.append(1)  # Adding a duplicate
    numbers = list(set(numbers))  # i use the set data structure which doesn't allow duplicates
    print(f"Numbers List (no duplicates): {numbers}")

    # Combine numbers and shoe_sizes into a third list
    combined_list = numbers + shoe_sizes
    print(f"Combined List: {combined_list}")

list_initialization_and_append()
