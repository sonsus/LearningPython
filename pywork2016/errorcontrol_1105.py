#dealing with exceptions
#try, except, else


#runtime error 
try:
	a=[1,2,3]
	a3=a[2]
	b=4/1
except ZeroDivisionError as e:
	print(e)
	print('zero division error')
except IndexError as k:
	print(k)
	print('index error occured')
else:
	print('no error here!')
#finally:
	print('finally block visited')
'''
like if, elif, else statements, 
except blocks are excecuted according to correspondence
after else block visited (that is, no error occurs here),
finally block is visited.
this is same for except bloc 

'''

