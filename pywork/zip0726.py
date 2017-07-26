lista=[i for i in range(1,5)]
listb="abcde"

zipped=list(zip(lista,listb))
print(zipped)


x,y=zip(*zipped)
print("x is same as lista, but in zip obj" ,list(x)==lista)
print("y is same as listb, but in zip obj", list(y)==listb)

print("what?")

print(lista)
print(listb)
print(list(x))
print(list(y))