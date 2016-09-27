#Given a string, print the Caesar Cipher (or ROT13) of that string.  Convert ! to ? and visa versa.
string = raw_input("Please give a string to convert: ").lower()
cipher_list = "nopqrstuvwxyzabcdefghijklm"
alpha_list = "abcdefghijklmnopqrstuvwxyz"
new_string = ""

for letter in string:
    if letter == "m":
        new_string += "z"
    elif letter == " ":
        new_string += " "
    elif letter == "!":
        new_string += "?"
    elif letter == "?":
        new_string += "!"
    elif letter not in alpha_list:
        print "Invalid character"
    else:
        i = cipher_list.index(letter)
        new_letter = alpha_list[i]
        new_string += new_letter
print new_string
