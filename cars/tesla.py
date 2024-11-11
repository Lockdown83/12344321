def draw_cross(size):
    if size % 2 == 0:
        raise ValueError("Size must be an odd number to draw a symmetrical cross.")
    
    cross = []
    for i in range(size):
        row = [' '] * size  # Create a row filled with spaces
        row[size // 2] = '*'  # Set the middle column to '*'
        cross.append(''.join(row))  # Join the row into a string
        
    cross[size // 2] = '*' * size  # Set the middle row to all '*'
    
    for line in cross:
        print(line)  # Print each line of the cross

# Example usage:
# draw_cross(5)  # This will draw a cross of size 5
