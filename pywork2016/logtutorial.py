import logging
import sys

logger=logging.getLogger('sth')
logger.setLevel(logging.DEBUG)

handler=logging.FileHandler('sth.log')
handler.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s : %(sys.stdout)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
#logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
#logging.debug('this is debug')
#logging.info('this is info')
#logging.warning('this is warning')
def gcd(a,b):
    while(a!=b):
        if a>b:
            a-=b
        else:
            b-=a
    return a
print('this is the program that prints GCD by Gaussian subtraction')
a=int(input('put an integer: '))
b=int(input('put another integer: '))
k='gcd of {0} and {1} is {result}'.format(a,b,result=gcd(a,b))
print(k)