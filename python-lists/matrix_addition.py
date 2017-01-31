print "Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as a list of lists:"

# With numpy
# import numpy as np
#
# Mat1 = np.matrix([[2, -2],
#           [5, 3]])
# Mat2 = np.matrix([[5, 2],
#           [1, 0]])
#
# print Mat1 + Mat2

# With empty matrix
Mat1 = [[2, -2],
        [5, 3]]
Mat2 = [[5, 2],
        [1, 0]]
sumMat = [[0,0],[0,0]]

for i in range(len(Mat1)):
    for j in range(len(Mat1[0])):
        sumMat[i][j] = Mat1[i][j] + Mat2[i][j]

for s in sumMat:
    print(s)



sumMat0 = (Mat1[0][0]+Mat2[0][0])
sumMat1 = (Mat1[0][1]+Mat2[0][1])
sumMat2 = (Mat1[1][0]+Mat2[1][0])
sumMat3 = (Mat1[0][0]+Mat2[0][0])
