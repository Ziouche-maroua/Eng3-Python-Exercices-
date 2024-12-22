# Exercise: Sorted List Builder

def sorted_list_builder():
    # Initialize an empty list to track numbers
    user_list = []

    while True:
        try:
            # Prompt the user for a number
            number = input("Enter a number (0 to quit): ").strip()
            
            # Check if the input is an integer
            number = int(number)

            if number == 0:
                print("Exiting...")
                break

            # Add the number to the list
            user_list.append(number)

            # Print the current and sorted lists
            print(f"Current List: {user_list}")
            print(f"Sorted List: {sorted(user_list)}")
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Bonus: Offer descending order and statistics
    print("Final Lists:")
    print(f"Ascending Order: {sorted(user_list)}")
    print(f"Descending Order: {sorted(user_list, reverse=True)}")

    if user_list:
        mean = sum(user_list) / len(user_list)
        median = sorted(user_list)[len(user_list) // 2] if len(user_list) % 2 != 0 else (
            sorted(user_list)[len(user_list) // 2 - 1] + sorted(user_list)[len(user_list) // 2]) / 2
        print(f"Mean: {mean}")
        print(f"Median: {median}")

    # Bonus: Save to file
    save_option = input("Do you want to save the lists to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open("sorted_list.txt", "w") as file:
            file.write(f"Current List: {user_list}\n")
            file.write(f"Sorted List (Ascending): {sorted(user_list)}\n")
            file.write(f"Sorted List (Descending): {sorted(user_list, reverse=True)}\n")
            file.write(f"Mean: {mean}\n")
            file.write(f"Median: {median}\n")
        print("Lists saved to 'sorted_list.txt'.")

sorted_list_builder()
