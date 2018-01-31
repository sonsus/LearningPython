import class1018 as cls
import arithmetics_classEx1018 as arith

ins1=cls.practice()
ins2=arith.Arithmetics()

lefttimeforme=ins1.timeleft()
ins2.set_data(10,20)
task=ins2.mul()

print("repeat coding which takes %s min for %s times"%(lefttimeforme,task))