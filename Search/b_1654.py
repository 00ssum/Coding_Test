import sys
input= sys.stdin.readline
k, n = map(int,input().split())
array=[]

for i in range(k):
    array.append(int(input()))
array.sort()

start=1
end=array[-1]
result=0

def l_n(h): #몇개의 렌선을 만들 수 있을지 계산하는 함수
    s=0
    for i in array:
        s+=i//h
    return s

while start <= end:
    mid = (start + end) // 2 #중간점
    if l_n(mid) >= n: # 중간점 값= 찾는값 => 찾기 완료
        result=mid
        start=mid+1

    else:# 중간점 값 < 찾는값
        end = mid - 1
print(result)
