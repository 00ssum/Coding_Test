import sys
input= sys.stdin.readline
n = int(input())
array=list(map(int, input().split()))
array.sort()
total=int(input())

start=1
end=array[-1]
result=0

def total_m(h): #총 들어가는 예산 계산 함수
    s=0
    for i in array:
        if i>h:
            s+=h
        else:
            s+=i
    return s

while start <= end:
    mid = (start + end) // 2 #중간점
    if total_m(mid) <= total: # 중간점 값= 찾는값 => 찾기 완료
        result=mid
        start=mid+1

    else:# 중간점 값 < 찾는값
        end = mid - 1
print(result)
