import math
import time

def isItPrime(num):
    root = int(math.floor(math.sqrt(num)))
    for i in range(2,root+1):
        if(num%i==0):
            #print str(i) + " goes into " + str(num)
            return False
    return True

n = 2
i = 3
timer = time.clock()
while(n<10001):
    i+=2
    if(isItPrime(i)):
        #print str(i) + " is prime"
        n+=1
        #print "n is now: " + str(n)
    
timer = time.clock()-timer

print "it took " + str(timer) + " seconds to find that " + str(i) + " is the " + str(n) + " prime"  

