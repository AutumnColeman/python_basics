print "Given an list of numbers, create a new list which contains every number in the given list which is positive."

lst = [-2, -42, 8, 42, 0, -1000, 1000000]
new_lst = []
for num in lst:
    if num >= 0:
        print num
