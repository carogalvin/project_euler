import math
import time

for n in range(1,1001):
    ans = .5*(-1*n+math.sqrt(n**2+2000))
    print str(n) + " " + str(ans)
