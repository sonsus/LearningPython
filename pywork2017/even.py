#squared number has 2k number of divisors

from math import sqrt

num_str=input()
num_list=num_str.split(' ')

a=int(num_list[0])
b=int(num_list[1])

count =0

for num in range(a,b+1):
    if sqrt(num)-int(sqrt(num))==0: 
        count+=1
        print(num, count)
print(count)