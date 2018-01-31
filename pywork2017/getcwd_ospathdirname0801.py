#os.getcwd() vs os.path.dirname(os.path.abspath(__file__))

import os

print("working dirname")
print(os.path.dirname(os.path.abspath(__file__)))
print("getcwd()")
print(os.getcwd())


'''
for windows getcwd() returns directory of running script

e.g.
> python pywork\\getcwd_ospathdirname0801.py

working dirname
C:\Users\SEONIL\Documents\LearningPython\pywork
getcwd()
C:\Users\SEONIL\Documents\LearningPython