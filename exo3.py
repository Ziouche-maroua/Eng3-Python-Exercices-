def calculate_discounted_price():
    
    total_amount = float(input("Enter the total amount of the purchase: $"))
    number_of_items = int(input("Enter the number of items: "))
    day_of_week = input("Enter the day of the week: ").strip().lower()

    # Determine the base discount
    discount = 20 if day_of_week in ["saturday", "sunday"] else 10

    
    if number_of_items > 5:
        discount += 5

    
    total_price = total_amount * (1 - discount / 100)

    print(f"Total price after discounts: ${total_price:.2f}")


calculate_discounted_price()
