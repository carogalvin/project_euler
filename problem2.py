
def evenFib(prev1, prev2, tot):
    print "First line"
    if(prev1+prev2 >= 4000000):
        print "reached end"
        print tot
        return tot
    elif( (prev1+prev2) % 2 == 0):
        tot += prev1+prev2
        print "found an even fib: " + str(prev1+prev2)
        print "new total: " + str(tot)

    evenFib(prev2, prev1+prev2, tot)

i=evenFib(1,2,2)
print i
