def print_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

# Example usage
print_triangle(5 * 2)