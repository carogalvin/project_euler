import math
import time

def isItPrime(num):
    root = int(math.floor(math.sqrt(num)))
    for i in range(3,root,2):
        if(num%i==0):
            return False
    return True

def checkPower(num,i):
    j=1
    while(num%(math.pow(i,j)) == 0):
        j+=1
    return (j-1)

ret = 1
num=600851475143
i=3
timer = time.clock()
while(i<int(math.floor(num/2))):
    #timer = time.clock()
    boo = isItPrime(i)
    #timer = time.clock()-timer
    #print "time taken for isItPrime(" + str(i) + "): " + str(timer)
    #print "checking " + str(i)
    if(num%i == 0 and boo):
        n=checkPower(num,i)
        #print "the prime power " + str(i) + "^" + str(n) + " is a factor"
        num=num/(math.pow(i,n))
        ret = i
    i+=2
if(isItPrime(num) and num>ret):
    ret = num
timer=time.clock()-timer
print timer
print ret
