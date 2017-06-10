import time

def collatz(n):
    ln = 0
    while(n != 1):
        if(n%2==0):
            n/=2
        else:
            n=3*n+1
        ln+=1
    return ln

longest=0
curr = 0
timer = time.clock()
for i in range(2,1000000):
    col = collatz(i)
    if(col>longest):
        longest=col
        curr=i
    if(time.clock()-timer > 60):
        print "timed out"
        break
print curr
print longest
