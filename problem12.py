import time
import math

# figure out if a number is prime
def isItPrime(num):
    root = int(math.floor(math.sqrt(num)))
    for i in range(2,root+1):
        if(num%i==0):
            return False
    return True

# make a list of the first n prime numbers
def primes(n):
    primes = [0]*100
    i=2
    while(n>0):
        if(isItPrime(i)):
            primes[-n]=i
            n-=1
        i+=1
    return primes

# find out how many times i goes into n
def powers(n,i):
    powr = 1
    new = i**2
    while(n%new==0):
        powr+=1
        new*=i
    return powr

# list of the first 100 prime numbers
prime = primes(100)

n = 1
tot = 2
tri = 0
timer = time.clock()

while(tot<=500):
    n+=1
    tri = n*(n+1)/2
    tot = 1
    for p in prime:
        if(tri%p==0):
            tot*=powers(tri,p)+1
    if(time.clock()-timer > 60):
        print "taking too long"
        break
print tri
print n
print tot
    
        
