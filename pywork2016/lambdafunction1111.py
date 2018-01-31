#lambdafunction.py
mylist=[lambda a, b: a+b, lambda a,b: a*b]
print(mylist)
print(mylist[0](2,3), mylist[1](3,4))
'''
lambda a, b: (a, b) # here the return is implicit
'''

print("two_times() output")

def two_times(list):
	result=[]
	for number in list:
		result.append(2*number)
	return result
print(two_times([1,2,3,4]))


print("map output")

def short_2times(x): return x*2
print(list(map(short_2times, [1,2,3,4])))


print("using lambda, reduce the code into 1 line!")
print(list(map(lambda x:x*2, [1,2,3,4])))
