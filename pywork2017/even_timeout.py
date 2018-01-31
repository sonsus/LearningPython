#timeout error
#program even

from math import sqrt

numstring=input()
numlist=numstring.split(' ')
a=int(numlist[0])
b=int(numlist[1])

def numDiv(num):
    count=0
    lim=int(sqrt(num))
    for i in range(1,lim+1):
        if num/i-int(num/i)==0: count+=1
    return count

corres=0
for num in range(a,b+1):
    divs=numDiv(num)
    if divs/2-int(divs/2)==0: corres+=1

print(corres)   