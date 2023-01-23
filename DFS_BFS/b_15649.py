#https://www.acmicpc.net/problem/15649

from itertools import permutations
n, m= map(int,input().split())
arr=[]
for i in range(1, n+1):
    arr.append(str(i))

p = list(map(' '.join, permutations(arr, m)))

for i in range(len(p)):
    print(p[i])
