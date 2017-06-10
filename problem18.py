
## opens the text file that contains the triangle of integers (separated by spaces)
## returns a matrix representation of it
def buildMatrix(filename):
    f = open(filename)
    numbers = f.readlines()
    f.close()

    for j in range(0, len(numbers)):
        numbers[j] = numbers[j].split()
        for i in range(0, len(numbers[j])):
            numbers[j][i] = int(numbers[j][i])
    return numbers

matrix = buildMatrix("p18triangle.txt")
#matrix = buildMatrix("p067_triangle.txt")
#print(matrix)
#print(matrix)
#matrix = buildMatrix("newgrid.txt")
##def findMaxSum(mtx):
##    maxsum = 0
##    for j in range(0, len(mtx)): #iterate through the indices of the last row
##        sum = mtx[len(mtx)-1][j]
##        prevind = j
##        for i in range(len(mtx)-1, 0, -1): #iterate backwards through the rows
##            if(prevind == 0): #the previous chosen value is the first in a row
##                sum+=mtx[i][0]
##            elif (prevind == i+1): #the previous chosen value is the last in a row
##                sum+=mtx[i][i]
##                prevind = i
##            else:
##                left = mtx[i][prevind-1]
##                right = mtx[i][prevind]
##                if (left > right):
##                    sum+=left
##                    prevind -=1
##                elif (right > left):
##                    sum+=right
##                else: #the case where we have to recurse to find the best choice
##                    
##        maxsum = max(maxsum, sum)

##def findMaxSum(row, col):
##    val = matrix[row][col]
##    #print(str(row) + "," + str(col)+","+str(val))
##    if(row == 0):
##        return val
##    else:
##        if(col == 0):
##            return val + findMaxSum(row-1, col)
##        elif (col == row):
##            return val + findMaxSum(row-1, row-1)
##        else:
####            left = matrix[row-1][col-1]
####            right = matrix[row-1][col]
####            if (left > right):
####                return val + findMaxSum(row-1, col-1)
####            elif (right > left):
####                return val + findMaxSum(row-1, col)
####            else:
##                return val + max(findMaxSum(row-1, col-1), findMaxSum(row-1, col))
##

def findMaxSum(row, col):
    val = matrix[row][col]
    if (row == len(matrix)-1):
        return val
    else:
        return val + max(findMaxSum(row+1,col), findMaxSum(row+1,col+1))
print(findMaxSum(0,0))
##maxi = 0
##for j in range(0,len(matrix)):
##    sum = findMaxSum(len(matrix)-1, j)
##    if(sum > maxi):
##        maxi = sum
##print(maxi)
