from bisect import bisect_left, bisect_right
n,t=map(int,input().split())
a=list(map(int,input().split()))

def c_b_r(a,l_v, r_v):
    r_i= bisect_right(a,r_v)
    l_i = bisect_left(a, l_v)
    if r_i-l_i!=0:
        print(r_i-l_i)
    else:
        print(-1)
    return 0

c_b_r(a,t,t)
