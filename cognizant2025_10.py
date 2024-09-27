def max_subarray_sum(arr):
    # Initialize current_sum and max_sum with the first element
    current_sum = max_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Decide whether to add the current number to the current subarray or start a new one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is greater than max_sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Input from user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
arr = list(map(int, user_input.split()))

# Calculate the maximum subarray sum
result = max_subarray_sum(arr)

# Print the result
print(f"The maximum subarray sum is: {result}")
