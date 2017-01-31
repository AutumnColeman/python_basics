print "Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list."

exampleList = [-1,0,1,1,2,3,4,5,6,7,7,7,8,8,9,10]

# With set function
# newList = set(exampleList)
#
# print newList

# With loop
newList = []

for i in exampleList:
    if not i in newList:
        newList.append(i)

print newList
