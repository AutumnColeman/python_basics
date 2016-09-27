#Given a string, print the string reversed.
string = raw_input("Give me a string: ")
#print string[::-1] easy way with slice
output = ""

for char in string:
    output = char + output

print output
