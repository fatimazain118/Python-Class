import inspect
import numpy as np
import sys
import os
from fractions import Fraction
import math

def myInspectFn():
    print("inside inspect function\n")

myInspectFn()
print(inspect.getsource(myInspectFn))  #this tells the implementation of our function
print(inspect.getsource(np))

#to know the path of particular module
print(np.__file__)  #every module has __init__.py which first executed when you import module

print(os.getpid())  #process id of current process

print(sys.version)
print(os.name)
#to get particular value of environment variable

print(os.environ.get("PATH"))
print(os.environ.get("USERNAME"))

os.environ["USERNAME"] = "Zainab"

print(os.environ["USERNAME"])

z= complex(3,4)

print(z.real, z.imag)
print(Fraction())
print(Fraction(8,6))
print(Fraction(3.14))
print(7070651414971679 / 2251799813685248)

x = 2.89

print(math.floor(x))
print(math.ceil(x))
print(math.log(8,2))
print(math.cos(30))
print(math.sqrt(25))
print(math.exp(0))
