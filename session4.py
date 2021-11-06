# Couple of attribute .. __file__ and __name__
import sys
#print("Print the file name of this script", __file__) #gives the complete dicrectory of this file
print("Print the file name of this script", __name__)
print("Print the file name of sys :", sys.__name__)

myStr1 = "My String 1"
myStr2 = "My String 2"

print(myStr1 + myStr2)  #here no space is given
print(myStr1, myStr2)  #here print automatically gives space between the strings and the next line
print("Size of myStr1:", sys.getsizeof(myStr1))

oneCharStr = "a"
print("oneChar", sys.getsizeof(oneCharStr))

twoCharStr = "ab"
print("twoChar", sys.getsizeof(twoCharStr))

threeCharStr = "abc"
print("threeChar", sys.getsizeof(threeCharStr))

nullCharStr = " "
print("nullChar", sys.getsizeof(nullCharStr))

print("Length of myStr1: ", len(myStr1))

#help(str) #str is a string object defined in python and help(str) looks for the docstrings of the object
print("Encoding of Python string:", sys.getdefaultencoding())  #in python we have utf-8 not ascii like C or C++

aTozStr = "abcdefg"
print("String Slicing: ", aTozStr[:-5:-1])  #end is exclusive so -4 tk he jaiga,

#Reserve the string
print(aTozStr[-1::-1])
print(aTozStr[::-1])

print(aTozStr[-100:100:]) # here we can go out of range