class name(object):
    """this is test class with parameter: __init__(self,param1,param2) """
    def __init__(self, name, datalist=[]):
        self.name = name
        self.datalist=datalist
    def whatclassdo(self):
        print(self.name + " flies")

class test:
    num=0

ins=name("dragonflies are")
ins.whatclassdo()
print(ins.__doc__)


ob0=test()
ob1=test()

print("initial attribute num:")
print("ob0.num=",ob0.num)
print("ob1.num=",ob1.num)

test.num+=3
ob1.num-=1

print("after test.num+3, ob1.num-1...")
print("ob0.num=",ob0.num)
print("ob1.num=",ob1.num)

'''
>>> person1 = name("jean")
>>> person2 = name("dean")
>>> person1.name
'jean'
>>> person2.name
'dean'
'''