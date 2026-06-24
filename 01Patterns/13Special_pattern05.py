num = int(input("Enter number: "))

# Calculate the size of the grid (always odd)5
size = 2 * num - 1

# Loop through each row
for i in range(size):
    # Loop through each column
    for j in range(size):
        
        # Find the distance from all 4 edges
        top = i
        bottom = (size - 1) - i
        left = j
        right = (size - 1) - j
        
        # The layer level is determined by the closest edge
        distance = min(top, bottom, left, right)
        
        # Print the corresponding number for that layer
        print(num - distance, end="")
        
    # Move to the next line after completing a row
    print("")
