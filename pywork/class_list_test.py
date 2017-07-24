class Point:
    """class attribute 
    test""" #this corresponds to instance.__doc__
    path=range(10000,200)
    dist=50000000

list_points=[]
for i in range(0,10):
    ins=Point()
    list_points.append(ins.dist-i)
    if i==9: print(ins.__doc__)
print(list_points)