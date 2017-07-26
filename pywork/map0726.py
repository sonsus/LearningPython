def func(x):
    return x*2

mapped=map(func, [1,2,3,4])
print(list(mapped))

#is equal to

a=[]
for i in [1,2,3,4]:
    a.append(func(i))

print(a)