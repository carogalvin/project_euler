import copy

##def findPerm3(str):
##    permList = []
##    lst = list(str)
##    while(''.join(lst) not in permList):
##        for i in range(len(lst)-1, 0, -1):
##            permList.append(''.join(lst))
##            hold = lst[i-1]
##            lst[i-1] = lst[i]
##            lst[i] = hold
##    return permList
##            
##def findPerm4(str):
##    lst = list(str)
##    permList = []
##    for i in range(0,len(lst)):
##        permList += map(lambda x: lst[i] + x, findPerm3(lst[0:i] + lst[i+1:len(lst)]))
##    return permList
##        
##
##print(findPerm4("abcd"))

def findPerm(str):
    lst = list(str)
    permList = []

    if(len(lst) == 1):
        return lst[0]
    else:
        for i in range(0,len(lst)):
            permList += map(lambda x: lst[i] + x, findPerm(lst[0:i] + lst[i+1:len(lst)]))
    return permList

perm10 = findPerm("0123456789")
print(perm10[999999])
