def separate_price():
    # Ask the user for the price in dinars
    price = float(input("Enter the price in dinars: "))
    
    # Separate the integer and decimal parts
    dinars = int(price)  # The integer part
    centimes = round((price - dinars) * 100)  # The decimal part, converted to centimes
    
    # Print the results
    print(f"Dinars: {dinars}")
    print(f"Centimes: {centimes}")

# Run the function
separate_price()
