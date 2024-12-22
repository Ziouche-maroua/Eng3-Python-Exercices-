def unique_word_counter():
    # Initialize an empty set to track unique words
    unique_words = set()
    total_words = 0  # To count total words entered

    while True:
        # Prompt the user for a word
        word = input("Enter a word: ").strip() # strip removes leading/trailing whitespaces
        total_words += 1

        # Check for duplicates
        if word in unique_words:
            print(f"You typed in {len(unique_words)} unique words.")
            print(f"Unique words (alphabetically): {sorted(unique_words)}")
            break
        else:
            unique_words.add(word)

    # Bonus: Save unique words to a file
    save_option = input("Do you want to save the unique words to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open("unique_words.txt", "w") as file:
            file.write("\n".join(sorted(unique_words)))
        print("Unique words saved to 'unique_words.txt'.")

unique_word_counter()
