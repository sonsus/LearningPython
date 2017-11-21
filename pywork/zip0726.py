import numpy as np 


lista=list(np.arange(1,4,0.5))
listb="abcde"

zipped=list(zip(lista,listb))
print(zipped)

print(zipped[0])
k=zipped[0]
print(zipped)

x,y=zip(*zipped)
print("x is same as lista, but in zip obj" ,list(x)==lista)
print("y is same as listb, but in zip obj", list(y)==listb)

print("what?")

#print(lista)
#print(listb)
print("could zip obj be interpreted as a nparray?")
print(type(np.array(x)))
print(np.array(x))
print(np.array(x)[0])
print(np.array(x))

#print(list(x))
#print(list(y))