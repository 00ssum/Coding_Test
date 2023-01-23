def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2 #중간점

    if array[mid] == target:# 중간점 값= 찾는값 => 찾기 완료
        return mid

    elif array[mid] > target:# 중간점 값 > 찾는값 : [시작] ~ [중간 -1]
        return binary_search(array, target, start, mid - 1)
        
    else:# 중간점 값 < 찾는값 : [중간+1] ~ [끝]
        return binary_search(array, target, mid + 1, end)
        
#----------------------------------------------------------------------------------
# n(원소의 개수) target(찾는 값) 입력
n, target = list(map(int, input().split()))

# 전체 원소
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1) #start:0 end:(N-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
