# Step 1: Get the number of blocks from the user
blocks = int(input("Enter the number of blocks: "))

height = 0
blocks_needed_for_layer = 1

# Step 2: Build layer by layer
while blocks >= blocks_needed_for_layer:
    blocks -= blocks_needed_for_layer
    height += 1
    blocks_needed_for_layer += 1

# Step 3: Output the result
print("The height of the pyramid:", height)