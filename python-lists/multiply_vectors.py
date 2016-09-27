print "Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists."

lst1 = [2, 4, 6]
lst2 = [3, 6, 9]
new_lst = []

for i in range(3):
    new_lst.append(lst1[i] * lst2[i])
print new_lst
