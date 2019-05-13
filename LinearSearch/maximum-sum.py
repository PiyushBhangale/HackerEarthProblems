n = int(input())
a = tuple(map(int, input().split()))
s = 0
c = 0
for i in range(n):
    if a[i] >= 0:
        c += 1
        s += a[i]
if s <= 0:
    print(max(a), "1")

else:
    print(s, c)
