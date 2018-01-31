#truncatable prime
from math import sqrt
from time import clock

start=clock()

def isTruncatable(prime,prime_list):
    str_p=str(prime)
    l=len(str_p)
    if str_p[0]==1 or str_p[-1]==1: return False
    elif '5' in str_p[1:-1]: return False
    else:
        for i in range(l):
            if int(str_p[i:]) not in prime_list: return False
        for j in range(1,l):
            if int(str_p[0:j]) not in prime_list: return False
        return True


prime_list=[2,3,5,7,11]
res_list=[]
cand=13
while True:
    if len(res_list)==11: break
    for ob in enumerate(prime_list):
        p=ob[1]
        if int(cand)%p==0: #int(cand/p)*p==cand:
            break
        elif ob[1]>sqrt(cand):
            prime_list.append(cand)
            if isTruncatable(cand,prime_list)==True: 
#                print(cand)
                res_list.append(cand)
            break
                
    cand+=2


res=0
for nums in res_list:
    res+=nums
print("the answer is %s"%res)
print("elapsed time is %s s"%(clock()-start))