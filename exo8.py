def fizz_buzz():
    
    number = int(input("Enter an integer number: "))
    
    # Check the divisibility conditions
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # If the number is not divisible by 3 or 5, print the number itself

# Run the function
fizz_buzz()
