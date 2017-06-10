
def sumFirstN(n):
    return (n/2)*(1+n)

def sumSquares(n):
    tot = 0
    for i in range(n+1):
        #print str(i**2)
        tot += i**2
    return tot
print str(sumFirstN(100)**2)
print str(sumSquares(100))
print (sumSquares(100) - sumFirstN(100)**2)
