
def factorial(n):
    if(n == 1):
        return n
    return n * factorial(n-1)

def sumdigits(m):
    if(m <= 10):
        return m
    return (m%10) + sumdigits(m/10)

print(sumdigits(factorial(100)))
