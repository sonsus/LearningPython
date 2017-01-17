#!/bin/python

a=range(0,10)
b=[i**2 for i in a if i%3==0]
print(b)

for i in b:
    if i<20: continue #skip the following lines of statements in the block and run a following cycle
    print(i, end=" ")

#only 36 and 81 are printed

c=[(i,j) for i in range(0,10)
        for j in range(10,20)]

print(c)

'''output: j iterates first
[(0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (1, 10), (1, 11), (1, 1
2), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15),
 (2, 16), (2, 17), (2, 18), (2, 19), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3
, 19), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (4, 19), (5, 10), (5, 11), (5, 1
2), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (5, 18), (5, 19), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15),
 (6, 16), (6, 17), (6, 18), (6, 19), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18), (7
, 19), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (9, 10), (9, 11), (9, 1
2), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18), (9, 19)]
your option? type dp or sum:

'''`


#args method is not seemed not useful for getting multiple input from the user.
def x(option, *args):
    if option=='sum':
        res=0
        for i in args:
            res+=i
        return res
    elif option=='dp':
    	return args
option=input('your option? type dp or sum: ')




