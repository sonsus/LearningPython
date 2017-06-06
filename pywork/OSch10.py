def FCFS(numlist):
    dist=0    
    for i,num in enumerate(numlist):
        dist+=abs(num-numlist[i+1])
        if i==len(numlist)-2: break
    print("total distance required for FCFS is", dist)
    return None

def SSTF(numlist):
    dist=0
    curr=numlist[0]
    mini=max(numlist)

    for i,num in enumerate(numlist):
        diff=abs(curr-num)
        if diff<mini: 
            mini= diff
            keep= num
        if i==len(numlist)-1:    
            curr= keep
            dist+=diff
            numlist.remove(keep)
    print("total distance required for SSTF is", dist)
    return None

if __name__=="__main__":
    numlist_str=[]
    with open("readdata.txt") as dat:
        numlist_str=dat.read().split(",")
    
    numlist=[]
    for entry in numlist_str:
        numlist.append(int(entry)) 
    
    while 1:
        userin=input("FCFS? SSTF? type what you want: ")
        if userin=="FCFS": FCFS(numlist)
        elif userin=="SSTF": SSTF(numlist) 
        elif userin=="quit": exit(1)