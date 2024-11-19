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
def tesla():
            
    def draw_cross(size):
    draw_cross(5)               




def main():
    tesla()  # Call the tesla function to execute its contents

# This block checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Execute the main function

# Example usage:
# draw_cross(5)  # This will draw a cross of size 5
    print("Drawing a cross of size:", size)  # Print the size of the cross being drawn
    print("Drawing a cross of size:", size)  # Print the size of the cross being drawn
    draw_cross(size)  # Call the draw_cross function to actually draw the cross
            def tesla():
                draw_cross(5)               