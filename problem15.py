import time

def lattice(pt,size):
    a = pt[0]
    b = pt[1]
    if(a == size and b == size):
        return 1
    elif(a == size):
        return lattice([a,b+1],size)
    elif(b == size):
        return 0
    else:
        return lattice([a+1,b],size) + lattice([a,b+1],size)


timer = time.clock()
lat = lattice([0,0],20)*2
timer = time.clock()-timer


print lat
print timer
print '\n'
