width = int(raw_input("Width?" ))
height = int(raw_input("Height?" ))
print "*" * width
for i in range(height - 2):
    num_spaces = width - 2
    spaces = " " * num_spaces
    row = "*" + spaces + "*"
    print row
print "*" * width
