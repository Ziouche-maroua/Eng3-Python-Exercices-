user_input = input("Enter a string in lowercase: ")

# Define the vowels we need to check
vowels = ['a', 'e', 'o']

# Check for each vowel and print the corresponding message
for vowel in vowels:
    if vowel in user_input:
        print(f"The vowel '{vowel}' is present in the string.")
    else:
        print(f"The vowel '{vowel}' is NOT present in the string.")
