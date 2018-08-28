

```python
*argv
def function(*argv):
    ...

a = (1,2,3) --> function(a)     arg1: 1
                                arg2: 2
                                arg3: 3

def function(**kwargs):
    ...

a = {"key1": 3,"key3": 1, "key2: 2} --> function(a)     "key1": 3
                                                        "key2": 2
                                                        "key3": 1
```
