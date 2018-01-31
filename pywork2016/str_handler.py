import logging
import sys

def gcd(a,b,stream):
    while(a!=b):
        print(stream)
        if a>b:
            a-=b
        else:
            b-=a
    return a

log = logging.getLogger()
log.setLevel(logging.DEBUG)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log.addHandler(stream)

gcd(128, 27, log)