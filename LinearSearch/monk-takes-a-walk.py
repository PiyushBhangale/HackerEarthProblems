# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/monk-takes-a-walk/
# Write your code here

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().rstrip().split())))
arr_count = []


def split(word):
    return [char for char in word]


for i in arr:
    counter = 0
    split_list = split(i[0])
    for v in vowels:
        count = split_list.count(v)
        counter += count
    print(counter)
