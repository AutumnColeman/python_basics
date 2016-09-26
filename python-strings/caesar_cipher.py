key_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

string = raw_input("What string? ").lower()
new_string = ""
for char in string:
    idx = key_list.index(char)
    real_idx = idx + 13
    for char in string:
        print new_string
