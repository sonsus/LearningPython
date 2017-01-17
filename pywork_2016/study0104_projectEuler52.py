#0104_projectEuler
import math as ma

def findsmallest(x):
	while True:
		print("current x is %s"%x)
		m=int(ma.log10(x))
		if int(ma.log10(6*x))>m: 
			x=10**(m+1)+1
			continue
		elif ()
		else:
			strlist1x=list(str(x))
			for i in range(2,7):
				stri=str(i*x)
				for j in range(0,m+1):
					if stri[j] in strlist1x: 
						strlist1x.remove(stri[j])
						if len(strlist1x)==0 and i==6: return x
					else: break
				break
		x+=1

if __name__=='__main__':
	x=11
	print(findsmallest(x))
	a=findsmallest(x)
	for i in range(2,7): print(a*i)
