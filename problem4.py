import math
import time

def isPalindrome(num):
    #print str(num)
    dig = int(math.log(num,10))
    alldig = []
    #print "there are " + str(dig) + " digits"
    for i in range(dig+1):
        newdig = (num/(10**i))%10
        #print str(newdig)
        alldig.append(newdig)
    #print alldig
    for i in (range(dig/2+1)):
        #print "checking if " + str(alldig[i]) + " at pos " + str(i) + " is the same as " + str(alldig[dig-i]) +" at pos " + str(dig-i)
        if (alldig[i] != alldig[dig-i]):
            return False
    return True

ans = 0
timer = time.clock()
for i in range(101,1000):
    for j in range(101,1000):
        #print str(i)
        #print str(j)
        if(isPalindrome(i*j) and i*j>ans):
           #print str(i*j) + " is a bigger palindrome"
           ans = i*j
timer = time.clock() - timer
print timer
print ans

#isPalindrome(11118)
