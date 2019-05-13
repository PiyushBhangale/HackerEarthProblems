n = int(input())
count = 0
while(n > 0):
    n -= 1
    a = list(map(int, input().rstrip().split()))
    if (a[0]/a[1] <= 1.7 and a[0]/a[1] >= 1.6) or (a[1]/a[0] <= 1.7 and a[1]/a[0] >= 1.6):
        count += 1

print(count)
