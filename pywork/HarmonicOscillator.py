import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.hermite as her
import math

#x is a list for x domain
#q order of a hermite polym(integer!)
def hermite_n(x,q):
    n=np.zeros(int(q))
    n[-1]=1
    y=her.hermval(x, n)
    return y

# x is a LIST for x domain
# q is state quantum no, /m is reduced mass of the molecule,/ omega is angular vib-freqency
def HOsln(x, q, m, omega):
    hbar=(6.626 * 10**(-34))/2*math.pi
    b=math.sqrt(m*omega/hbar)
    wav = (math.sqrt(math.factorial(q) * 2**(q)))**(-1) * (b**2/math.pi)**(1/4) * hermite_n(b*x,q) * np.exp(-b*b*x*x/2)
    return wav


x=np.linspace(-10**(-9),10**(-9),1000)
m=float(input('reduced mass in amu? '))
m*=1.66*10**(-27)
q=int(input('state quantum number(integer)? '))
w=float(input('vibrational frequency(cm-1) '))
w*=100*2*math.pi*2.997*10**(8)


plt.title('Harmonic oscillator '+'%i''th state prob density'%q)
plt.plot(x,HOsln(x,q,m,w)**2)
plt.show()
