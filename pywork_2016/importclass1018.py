#import module
import sys
sys.path.append("C:/Users/xozmf/Documents/2016-2/pywork")
#sys.path.append is temporary. Not permanent.
import arithmetics_classEx1018 as arith


if __name__=="__main__":
    P=arith.Arithmetics()
    print(arith.P.sum())
    print(arith.P.div())