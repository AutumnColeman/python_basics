print "Given an list of numbers, print each number in the list that is greater than zero."

lst = [-2, -42, 8, 42, 0, -1000, 1000000]
new_lst = []
for num in lst:
    if num > 0:
        print num
