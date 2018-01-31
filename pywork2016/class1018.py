#Python has no private class variable. It is vulnerable and we should be careful manipulating class vars.
#Naming convention for mem. var. wamted to be protected is that dunder starting name (e.g. __var)
#

#Class in python

class practice:
    used=0 #they are in default public.
    time=2

    def __init__(self): #always being executed during every instantiation
    	self.time=2

    def timeleft(self):
        ihave=self.time-self.used
        return ihave
    def set_used(self,howmany):
    	self.used=howmany


if __name__=="__main__":
	me1=practice()
	print(me1.timeleft()) #expected 2
	me1.used=1
	print(practice.used) #expected 0
	print(me1.used) #expected 1

#changing the member var (all instances declared after this will be influenced)
	practice.used=1
	me2=practice()
	print(me2.timeleft()) #expected 1
	practice.used=2
	me3=practice()
	print(me3.timeleft()) #expected 0




