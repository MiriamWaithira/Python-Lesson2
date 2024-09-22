# Create a list of integers and compute their sum
# Initialize an empty list to store the integers
integers_list = []

# Accept user input of multiple integers in one go
user_input = input("Enter integers separated by spaces (or type 'done' to finish): ")

# Check if the user wants to finish right away
if user_input.lower() != 'done':
    try:
        # Split the input by spaces, convert each to an integer, and add to the list
        integers_list = [int(num) for num in user_input.split()]
    except ValueError:
        print("Please enter valid integers separated by spaces.")

# Calculate the sum of all integers in the list
total_sum = sum(integers_list)

# Print the list and its sum
print(f"List of integers: {integers_list}")
print(f"Sum of all integers: {total_sum}")


# Run the code in Terminal