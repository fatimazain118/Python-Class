i=-2
print(abs(i))  #print absolute value
print(bin(5))  #binary representation of no.
print(divmod(10,5))  #gives division and remainder
print(int(-10))
print(pow(2,3))
#----------------------
#homeWork

j=3
k=9.0
m=i+j+k
print(type(i))
print(type(k))
print(type(m))
v=9.0
print(id(k))  #this id gives the label/address k and v gives same as pointing to same float no. in memory
print(id(v))  #could be any dynamic location in the memory

#we need to use new version of python because (3.8.8) as python is open source and developers around the globe are contributing to the python lib, also your compiler version should match with the code we right here else it'll show error
print("Hi") #here we use build-in function which is interpreting it converting it into byte code pvm is running in the background and gives the CPU to run this line and gives output

print(__doc__)  #docstring
print(type(type))  #it's from class type
print(print.__doc__)  #as print itself is a class

import sys
myNum = 4
print(sys.getsizeof(myNum))  #Return the size of object in bytes

print(hex(16))
print(hex(0x10))
print(int("22", base =0))  #you cannot give base=1 must be>=2 or <=36, or 0
print(int("22", base =10))
print(int("22", base=3))   #2 * 3^1 +2 ==8
#z==35 value
print(int("zzz", base=36))  #35* 36^2 + 35* 36^1 + 35 ==46655, this base is default parameter
print(int("11", base=2))  #base2 means binary no. which accept only 0 or 1 we cannt have 22 in place of 11++