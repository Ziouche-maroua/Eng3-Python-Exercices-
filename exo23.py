# Function to get a positive integer input from the user
def get_positive_integer():
    while True:
        try:
            # Ask for input
            N = int(input("Please enter a positive integer: "))
            
            # Check if the input is positive
            if N > 0:
                return N
            else:
                print("The number must be positive. Please try again.")
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter a valid positive integer.")

# Get the positive integer from the user
N = get_positive_integer()

# Print numbers from -N to N, excluding 0
for i in range(-N, N + 1):
    if i != 0:
        print(i)
