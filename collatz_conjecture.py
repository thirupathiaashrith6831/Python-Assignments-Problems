# Get the initial number from the user
c0 = int(input("Enter a non-negative, non-zero integer: "))

# Initialize the step counter
steps = 0

# The loop runs until the number hits 1
while c0 != 1:
    # Check if c0 is even
    if c0 % 2 == 0:
        c0 = c0 // 2  # Use integer division //
    # Otherwise, it must be odd
    else:
        c0 = 3 * c0 + 1
    
    # Print the current value and increment the step count
    print(c0)
    steps += 1

# Finally, print the total number of steps
print("steps =", steps)