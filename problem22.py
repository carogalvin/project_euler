
namesFile = file('p022_names.txt')
namesString = namesFile.readline()
namesFile.close()
namesList = map(lambda x: x[1:-1], namesString.split(',')) #split the one giant line into a list of names, then trim the quotation marks

def partition(lst, lo, hi):
    piv = lst[hi]
    i = lo
    for j in range(lo, hi):
        if(lst[j] <= piv):
            holder = lst[i]
            lst[i] = lst[j]
            lst[j] = holder
            i+=1
    holder = lst[i]
    lst[i] = lst[hi]
    lst[hi] = holder
    return i

def quicksort(lst, lo, hi):
    if(lo < hi):
        piv = partition(lst, lo, hi)
        quicksort(lst, lo, piv-1)
        quicksort(lst, piv+1, hi)

def namescore(str):
    tot = 0
    for char in str:
        tot += ord(char)-64
    return tot
print(namescore("COLIN"))
tot = 0
quicksort(namesList, 0, len(namesList)-1)
for i in range(0,len(namesList)):
    tot += namescore(namesList[i]) * (i+1)
print(tot)

