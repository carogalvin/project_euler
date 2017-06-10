import math
fibList = [1, 1]

def genNextFib():
    return fibList[-1] + fibList[-2]

nextFib = genNextFib()
while(math.floor(math.log(nextFib, 10) + 1) < 1000):
    fibList.append(nextFib)
    nextFib = genNextFib()
print(len(fibList))
