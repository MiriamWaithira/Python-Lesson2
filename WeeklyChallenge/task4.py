# Create two sets and find common elements

# Function to get a set of integers from user input
def get_set():
    user_set = set()
    while True:
        user_input = input("Enter an integer for the set (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            # Convert input to an integer and add it to the set
            number = int(user_input)
            user_set.add(number)
        except ValueError:
            print("Please enter a valid integer.")
    return user_set

# Create the first set
print("Create the first set:")
set1 = get_set()

# Create the second set
print("Create the second set:")
set2 = get_set()

# Find the common elements between the two sets
common_elements = set1.intersection(set2)

# Print the sets and their common elements
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Common elements: {common_elements}")

# Run the program from the Terminal