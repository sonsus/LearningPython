try:
    4/0
    a = [1,2]
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)