

filename="D:\Dropbox\ProjectEuler\p10grid.txt"
grid = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ]

tgrid = [ [2,1,1,1,1],[10,1,4,1,1],[1,10,1,1,1],[1,1,10,1,1],[1,1,1,10,3]]
dim = len(grid)
f = open(filename)
tot=0
 #setup grid
for row in range(0,dim):
    line = f.readline()
    line = line.split(' ')

    for col in range(0,dim):
        grid[row][col] = int(line[col])
f.close()

# find the product of a list of numbers
def findprod(lst):
    prod = 1
    i=0
    while(i<len(lst)):
        prod*=lst[i]
        i+=1
    return prod

# find biggest product in cols
big = 0

for j in range(0,dim):
    for i in range(4,dim+1):
        curr = findprod(grid[j][i-4:i])
        tot+=1
        if(curr > big):
            big = curr

# find biggest product in rows

for i in range(0,dim):
    for j in range(4,dim+1):
        curr = findprod( [grid[j-4][i],grid[j-3][i],grid[j-2][i],grid[j-1][i]] )
        tot+=1
        if (curr > big):
            big = curr

# find biggest product in diagonal L->R

for i in range(0,dim-3):
    for j in range(0,dim-3):
        curr = findprod([ grid[i][j],grid[i+1][j+1],grid[i+2][j+2],grid[i+3][j+3] ] )
        tot+=1
        if (curr > big):
            big = curr

# find biggest product in diagonal R->L

for i in range(0,dim-3):
    for j in range(dim-1,2,-1):
        curr = findprod([ grid[i][j],grid[i+1][j-1],grid[i+2][j-2],grid[i+3][j-3] ] )
        tot+=1
        if (curr > big):
            big = curr

print big
print (tot == 17*20*2+17*17*2)
