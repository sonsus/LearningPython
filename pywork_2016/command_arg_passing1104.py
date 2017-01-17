#getting args from command line

import sys
#sys.path.append('C:/Users/xozmf/Documents/2016-2/pywork')
#above is how to add wanted path temporarily: that is, only during program running.

def test(option, *x): #*parameter is tuple containing whatever type of data like int or double or float.
	if option=='display':
		print(x) #parameter passed here is recognized as tuple. Let's see what happens
		print(type(x))
		return None
	elif option=='average':
		sum=0
		for items in (x): #here, we use x instead of *x. I dunno why.
			if type(items)!=type(1.0): 
				print('error! argument cannot be averaged') 
				return None
			else:
				sum+=items
	else:
		print("no such an option!")
		return None
	return sum/len(x)

if __name__=='__main__':
	a=test(sys.argv[1], 1.1,2.2,3.3,4.4)
	print(a)

