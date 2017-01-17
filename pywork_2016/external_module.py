#external functions 0102

import sys
import os
import pickle

print("sys.argv pass the parameters from the command line delimited by whitespaces")
print(sys.argv)

print("sys.exit() force-ends program")

print("sys.path shows the path we are working on. temporarily adding working directory is possible")
print("print(sys.path)")
print(sys.path)
sys.path.append("C:/Python/Python36-32")
print("append(\"C:/Python/Python36-32\")\n print(sys.path)")
print(sys.path)