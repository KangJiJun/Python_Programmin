# for

# for x in iterable object:
#   ...
for i in range(5): # 0 4
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(5,0,-1):
    print(i)

# 1~10 sum
s = 0
for i in range(1,11):
    s+=i
print(s)
print(sum(range(1,11)))

s = "Marinette 사랑해 愛情"
for c in s:
    print(c,end='')
print()
for i in range(72):
    print(f"{i//9+2:1d} * {i%9+1:1d} = {(i//9+2)*(i%9+1):2d}",end = ' ' if (i+1)%9 else '\n')
