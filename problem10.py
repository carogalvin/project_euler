import math
import time

def isItPrime(num):
    root = int(math.floor(math.sqrt(num)))
    for i in range(2,root+1):
        if(num%i==0):
            return False
    return True

i = 3
sum=2
timer = time.clock()
while(i<2000000):
    if(isItPrime(i)):
        sum+=i
    i+=2 
timer = time.clock()-timer

print "it took " + str(timer) + " seconds to find that the sum of all numbers below 2000000 is " + str(sum)
