# Datatype of python
# 1. Basic: Number(integer,real number) ,boolean, string
# 2. Collection: list, tuple, dictionary, set

# number(integer)
# int

a = 10
print(a)
print(a**a)

#bina, octa, hexa
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))

# integer range

x = 10 ** 100
print(x)

# Overflow
a = 2**31-1
print(a)
a += 1
print(a)

# Real number(float)
b = 3.14
print(b,type(b))

# float range
# floating point method: 64bit = sign(1bit)+exp(11bit)+mantissa(52bit)
b = 3.14159265358979323846264339

x=y=0.1
print(x+y==0.2)

import sys
print(sys.float_info.min)
print(sys.float_info.max)

a=1.7e308
b=1.8e308
print(a,b)

print(0.1+0.2)
print(0.1+0.2==0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")

print(float(10))
print(int(3.14))
print(int("100"))
print(float("3.14"))