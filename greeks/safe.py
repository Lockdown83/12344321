def draw_cross(size):
    """
    Draw a cross of a given size.

    Parameters:
    size (int): The size of the cross. It should be an odd number to ensure symmetry.

    Returns:
    None
    """
    if size % 2 == 0:
        raise ValueError("Size must be an odd number for symmetry.")

    for i in range(size):
        for j in range(size):
            if j == size // 2 or i == size // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row

# Example usage:
# draw_cross(5)
