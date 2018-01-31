#Four arithmetics

class Arithmetics:
    a=0
    b=0
    #without __init__, initialization works as declared above
    
    def __init__(self,dat1=0,dat2=0):
        a=dat1
        b=dat2
        return None
        
    def set_data(self,dat1,dat2):
        self.a=dat1
        self.b=dat2
        return None
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b!=0: pass
        else: 
            print("error! cannot div by 0") #printed
            return None
        return self.a/self.b

#if we dont want to execute below when only opened this file, not imported by others
if __name__=="__main__":
    A=Arithmetics(3,4)
#let us see how initialization works when we dont define init manually
    print(A.a)
    print(A.b) #initialization as declared.
   # A.set_data(1,0) 
#same as the expression on the right:   Arithmetics.setdata(A,1,2)
    print(A.add())
    print(A.sub())
    print(A.mul())
    print(A.div())

#Inheritance?
    print("inheritance test")
    class test(Arithmetics):
        pass
        def testprint(self):
            print(self.a)
            print(self.b)

    I=test()
    I.testprint() 
    #output: 
    #1
    #0