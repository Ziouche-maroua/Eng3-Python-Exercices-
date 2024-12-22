# Exercise: Interactive List Operations

def interactive_list_operations():
    # Initialize the list
    numbers = [1, 2, 3, 4, 5]

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Append")
        print("2. Insert")
        print("3. Pop")
        print("4. Remove")
        print("5. Quit")

        # Get the user choice
        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                # Append an element
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print(f"Updated List: {numbers}")

            elif choice == 2:
                # Insert an element
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index to insert at: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: Index out of range.")

            elif choice == 3:
                # Pop an element
                if numbers:
                    index = int(input("Enter index to pop (leave empty for last element): ") or -1)
                    if index == -1:
                        value = numbers.pop()
                    elif 0 <= index < len(numbers):
                        value = numbers.pop(index)
                    else:
                        print("Error: Index out of range.")
                        continue
                    print(f"Popped value: {value}")
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: List is empty. Cannot pop.")

            elif choice == 4:
                # Remove an element
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: Value not found in the list.")

            elif choice == 5:
                # Quit
                print("Exiting the program.")
                break

            else:
                print("Error: Invalid choice. Please select a valid option.")

        except ValueError:
            print("Error: Please enter a valid integer.")

interactive_list_operations()
