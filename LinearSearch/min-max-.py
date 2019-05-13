n = int(input())

a = (list(map(int, input().rstrip().split())))


print(sum(a)-min(a), sum(a)-max(a))
