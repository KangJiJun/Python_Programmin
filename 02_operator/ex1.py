# Operator

# Arithmetic Operator

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a ** b)

a = 0
a += 4
print(a)

a-=2
print(a)

# I/D operator

# Comparing operator
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3)    # 1 < 2 and 2 < 3
print(1 < 3 < 2)    # 1 < 2 and 2 < 3

# Logic operator (and,or,not)

a = True
b = False
print(a and b)
print(a or b)
print(not b)

# Short-circuit evaluation
a = 10
b = 0
# print(a / b)

if a < 10 and a / b > 0:
    print(a / b)
else:
    print(a)
