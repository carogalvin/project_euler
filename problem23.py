import math

def listDiv(n):
    div = [1]
    cap = math.sqrt(n)
    for i in range(2,int(cap)+1):
        if(n % i == 0):
            div.append(i)
            if(i != n/i):
                div.append(n/i)
    return div

def sumList(lst):
    tot = 0
    for i in lst:
        tot += i
    return tot

def sumDiv(n):
    return sumList(listDiv(n))

def abund(n):
    return sumDiv(n) > n

lista = [0]*28123
for i in range(12, 28123):
    if(abund(i)):
        lista[i] = 1

cant = 0
for i in range(1,28123):
    flag = False
    for j in range(0,i/2+1):
        if(lista[j]):
            if(i-j < len(lista)):
                flag = lista[i-j]
                if(flag):
                    break
    if(not flag):
        cant+=(i)
print(cant)
