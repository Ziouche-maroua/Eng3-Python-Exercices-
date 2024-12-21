def update_list():
    # Initialized list
    numbers = [1, 2, 3, 4, 5]

    while True:
        
            
        index = input("Enter index (-1 to quit): ")

        # Exit condition
        if index == "-1":
            print("Exiting...")
            break

        # Validate the index
        if not index.lstrip("-").isdigit():
            raise ValueError("Index must be an integer!")

        index = int(index)

        # Check if the index is within range
        if index < 0 or index >= len(numbers):
            print("Index out of range. Please try again.")
            continue

        # Ask for the new value
        new_value = input("Enter new value: ")
        if not new_value.isdigit():
            raise ValueError("The input should be an integer value!")

        numbers[index] = int(new_value)

        # Print the updated list
        print(numbers)
        

update_list()
