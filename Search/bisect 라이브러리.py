from bisect import bisect_left,bisect_right

def count_by_r(a,left_v,right_v):
    right_i=bisect_right(a,right_v)
    left_i=bisect_left(a,left_v)
    return right_i-left_i
