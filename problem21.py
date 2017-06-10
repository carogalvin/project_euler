import math

def listDiv(n):
    div = [1]
    cap = math.floor(math.sqrt(n))
    for i in range(2,int(cap)):
        if(n % i == 0):
            div.append(i)
            div.append(n/i)
    return div

def sumList(lst):
    tot = 0
    for i in lst:
        tot += i
    return tot

amicNum = []
for i in range(1, 10000):
    sumDiv = sumList(listDiv(i))
    #print("sum of divisors of " + str(i) + " is " + str(sumDiv))
    revSumDiv = sumList(listDiv(sumDiv))
    #print("sum of divisors of " + str(sumDiv) + " is " + str(revSumDiv))

    if(revSumDiv == i and i != sumDiv):
        print("found amicable numbers!: " + str(i) + " " +  str(sumDiv))
        amicNum.append(i)
print(amicNum)
print(sumList(amicNum))
