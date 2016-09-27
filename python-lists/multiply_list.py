print "Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list using console.log(list);"

factor = int(raw_input("What factor? "))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = []
for num in lst:
    new_lst = num * factor
    print new_lst
