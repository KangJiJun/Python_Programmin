# Bit operation
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b) 
print(40 >> b)
print(~a)

# Membership operator
print("a" in "apple")
print(3 in [1,2,3])

# Three-operand operator
mx = a if a > b else b

# "Even" when a is even, or else "Odd"
print("Even" if ~a & 1 else "Odd")

g = ['A','B','C']

score = 85
print(g[9 - score//10] if 70 <= score <= 100 else 'D')