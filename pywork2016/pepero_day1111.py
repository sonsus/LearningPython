#!/usr/bin/env python
 


#built in functions
abs(-1)==1
all([1,2,3,4])==True
all(0,1,2,3,4,5)==False
any(0,1,2,3)==True
chr(97)=='a'
dir([1,2,3])==['append', 'count', 'extend', 'index', ...]
divmod(4,3)==(1,1)
divmod(1.3,0.2)==(6.0,0.1)
enumerate(['a','b','c']) #returns enumerate object
eval('1+2') # returns executed result of a given string 
filter(function_name,iterable_inputs) # return inputs that results True for given function.

'''
def ispositive(x):
	return x>0

print(list(filter(ispositive, [-1,0,1,2,3,4])))


#resulted printout:
1,2,3,4
'''
hex(16)==0x10
id(3) # returns its address
\pass by reference
http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

summary: limited to mutable types of objects, by its method, we can change the content by reference

#if I still want to change the imutable things
#1.use return!
#2.or create a class that contains the data and a proper method.

class Person: pass
a=Person()
#then
isinstance(a, Person)==True

lambda #similar to def but inline function generation
lambda param1, param2, param3... : param1+param2*param3



len('string')
len([1,2,3,4])
len((2,3,4,5))          2,3,4,5 is actually a tuple but after ( of functioncall, it works in somewhat funny way.


fopen(file.txt, 'rb') #or 'wb' reading/ writing in binary mode
# makes no difference in Unix system since they only read/write files in binary mode. 
\But, in window linefeed will be changed into \r\n if not opened in binary mode

range(start=0, end(exclusive), interval)
