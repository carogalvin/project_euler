filename = "D:\Dropbox\ProjectEuler\p13numbers.txt"

f = file(filename)

lines = f.readlines()

f.close()
tot=0
i=0
while(i<len(lines)):
    lines[i] = int(lines[i])
    tot+=lines[i]
    i+=1
print tot

