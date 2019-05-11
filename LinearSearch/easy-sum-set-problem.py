n = input()
a = list(map(int, input().rstrip().split()))
m = input()
c = list(map(int, input().rstrip().split()))
b = []
for i in c:
    for j in a:
        if(i > j):
            b.append(i-j)
b = list(set(b))
z = []
for i in a:
    for j in b:
        if(c.count(i+j) == 0):
            z.append(j)
z = list(set(z))
for i in z:
    b.remove(i)
b.sort()
print(*b)
