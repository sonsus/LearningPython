#Nested function

1.Inner functions can access variables from the enclosing scope (in this case, the local variable x). If you're not accessing any variables from the enclosing scope, they're really just ordinary functions with a different scope.
2.Readability
http://stackoverflow.com/questions/1589058/nested-function-in-python


```python
def make_adder(x):
    def add(y):
        return x + y
    return add

plus5 = make_adder(5)
print(plus5(12))  
```
[out] 17
