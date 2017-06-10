import math

n=1
while(True):
    tot = 0
    for r in range(2,n):
        tot+= math.factorial(n)/( math.factorial(r)*math.factorial(n-r))
    if(tot >=250):
        print n
        break
