height = 5

for row_number in range(height):
    num_stars = (row_number * 2) + 1
    base_width = 2 * height - 1
    num_spaces = (base_width - num_stars) / 2
    spaces = " " * num_spaces
    stars = "*" * num_stars
    print spaces + stars
