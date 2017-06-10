
num_let_teen=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]

num_let_tens=[0,0,6,6,5,5,5,7,6,6]

num_let_hund=7

num_let_thou=8

num_let_and=3

def findNumLet(n):
    tot=0
    
    dig=[0,0,0,0]

    dig[3]=n%10
    dig[2]=(n/10)%10
    dig[1]=(n/100)%10
    dig[0]=n/1000
    print dig
    # case: we have a thousands digit
    if(dig[0]!=0):
        tot+= num_let_thou + num_let_teen[dig[0]]
    # case: we have a hundreds digit    
    if(dig[1]!=0):
        tot+=num_let_hund + num_let_teen[dig[1]]
    # case: we have a tens digit
    if(dig[2]!=0):
        # case: the tens digit is 1 (we have a "teen")
        if(dig[2]==1):
            tot+=num_let_teen[10+dig[3]]
        # case: the tens digit is not 1
        else:
            tot+=num_let_tens[dig[2]]
    # case: we don't have a "teen" but we have a ones digit
    if(dig[3]!=0 and dig[2]!=1):
        tot+=num_let_teen[dig[3]]

    # case: we need an "and"
    if((dig[0]!=0 or dig[1]!=0) and (dig[2]!=0 or dig[3]!=0)):
        tot+=num_let_and

    return tot

n=1
tot=0
while(n<1001):
    tot+=findNumLet(n)
    n+=1
print tot
