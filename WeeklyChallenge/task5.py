# Filter words with odd number of characters

# List of words which are fruits
words = ["apple", "banana", "cherry", "strawberry", "yellowmellon", "grape"]

# Use list comprehension to create a new list with words having an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the original list and the filtered list
print(f"Original list: {words}")
print(f"Words with an odd number of characters: {odd_length_words}")