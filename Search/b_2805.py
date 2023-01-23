import sys
input= sys.stdin.readline
n,m = map(int,input().split())
array= list(map(int, input().split()))
array.sort()

start=0
end=array[-1]
result=0

def m_t(h):
    s=0
    for i in array:
        if i>h:
            s+=(i-h)
    return s

while start <= end:
    mid = (start + end) // 2 #중간점
    if m_t(mid) >= m: # 중간점 값= 찾는값 => 찾기 완료
        result=mid
        start=mid+1

    else:# 중간점 값 < 찾는값
        end = mid - 1
print(result)
