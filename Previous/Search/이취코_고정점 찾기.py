'''
1. 중간값을 중간점으로
2. 중간점 값이 인덱스 값보다 작으면 왼쪽 버림
3. 중간점 값이 인덱스 값보다 크면 오른쪽 버림
'''
# n(원소의 개수) target(찾는 값) 입력
n = int(input())
# 전체 원소
array = list(map(int, input().split()))

def bina_s(array,start,end):
    while start <= end:
        mid = (start + end) // 2 #중간점
        if array[mid] == mid: # 중간점 값= 찾는값 => 찾기 완료
            return mid

        elif array[mid] > mid: # 중간점 값 > 찾는값
            end = mid - 1 #end 수정

        else:# 중간점 값 < 찾는값
            start = mid + 1 #start 수정
    return None

index= bina_s(array,0,n-1)

if index!=None:
    print(index)
else:
    print(-1)
