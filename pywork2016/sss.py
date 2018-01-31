from time import time
start=time()
x=11
while True:
    if (all (number in str(x) for number in str(2*x))):
        if (all (number in str(2*x) for number in str(3*x))):
            if (all (number in str(3*x) for number in str(4*x))):
                if (all (number in str(4*x) for number in str(5*x))):
                    if (all (number in str(5*x) for number in str(6*x))):
                        print(x)
                        break

    x += 1
print(time()-start)