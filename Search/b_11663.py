import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())

dit=list(map(int,input().split()))
dit.sort()
arr=[input().split()for _ in range(m)]

def count(arr,r_v,l_v):
    l_i=bisect_left(arr,l_v)
    r_i=bisect_right(arr,r_v)
    return r_i-l_i

for i in range(len(arr)):
    c=count(dit,int(arr[i][1]),int(arr[i][0]),)
    print(c)
