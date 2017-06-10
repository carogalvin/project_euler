
def sumDigits(n):
    tot = 0

    while(n>0):
        tot += n%10
        n=n/10

    return tot

print sumDigits(2**1000)
