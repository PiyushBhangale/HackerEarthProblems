'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import re
import functools
import operator
from collections import Counter

n = int(input())

lis, b_lis, g_lis = [], [], []
for _ in range(n):
    lis.append(input())
f = True
t = True
ini_g = None
ini_b = None
for i in lis:
    if "G:" in i:
        g_lis.append([int(s) for s in i.split() if s.isdigit()])
        while f:
            for s in i.split():
                if s.isdigit():
                    ini_g = int(s)
                    f = False

    if "M:" in i:

        b_lis.append([int(s) for s in i.split() if s.isdigit()])
        while t:
            for s in i.split():
                if s.isdigit():
                    ini_b = int(s)
                    t = False

fin_g_count = functools.reduce(operator.iconcat, g_lis, [])
fin_b_count = functools.reduce(operator.iconcat, b_lis, [])

weitage_g = ((fin_g_count.count(ini_g))*2)
weitage_b = (((fin_b_count.count(ini_b))*2)+(fin_g_count.count(ini_b)))

if weitage_g > weitage_b:
    print("Date")
else:
    print("No Date")
