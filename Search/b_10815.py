import sys
from bisect import bisect_left, bisect_right
input= sys.stdin.readline
n = int(input())
my= list(map(int, input().split()))
m = int(input())
search= list(map(int, input().split()))

my.sort()
def c(a,left_v, right_v):
    right_i=bisect_right(a, right_v)
    left_i=bisect_left(a, left_v)
    return right_i-left_i

for i in search:
    index=c(my,i,i)
    if index!=0:
        print(1,end=" ")
    else:
        print(0,end=" ")
