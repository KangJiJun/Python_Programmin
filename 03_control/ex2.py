# Loop : while, for

# while
i = 1
while i <= 10:
    print(i)
    i+=1
    if i == 11:
        break
else:
    print("End")
n = [1,3,5,7,9]
t = 3
i = 0
while i < 5:
    if n[i]==t:
        print("Found")
        break
    i+=1
else:
    print("Not Found")

i = 1
ans = 0
while i <= 10:
    ans += i if ~i&1 else 0
    i+=1
print(ans)
i=1
ans = 0
while i <= 10:
    ans += i if i&1 else 0
    i+=1
print(ans)