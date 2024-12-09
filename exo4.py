def compare_ages():
    # Get input for both ages
    age1 = int(input("Enter the age of the first person: "))
    age2 = int(input("Enter the age of the second person: "))
    
    # Compare ages and print the result
    if age1 > age2:
        print("The first person is older.")
    elif age2 > age1:
        print("The second person is older.")
    else:
        print("Both people are the same age!")

# Run the function
compare_ages()
