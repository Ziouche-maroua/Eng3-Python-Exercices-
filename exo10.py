def is_palindrome():
   
    word = input("Please enter a word to check if it's a palindrome: ").strip()

    # Initialize the palindrome flag
    is_palindrome = True

    # Loop through the first half of the word
    for i in range(len(word) // 2):
        # Compare characters from start and end using negative indexing since the last element in an array is by convention at index -1
        if word[i] != word[-(i + 1)]:
            is_palindrome = False
            break

    # Output the result
    if is_palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

# Run the palindrome checker
is_palindrome()
