def anagrams(str1, str2):
    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Test cases
print(anagrams("tame", "meta"))  # True

print(anagrams("tabby", "batty"))  # False

