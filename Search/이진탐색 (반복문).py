def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 #중간점
        if array[mid] == target: # 중간점 값= 찾는값 => 찾기 완료
            return mid

        elif array[mid] > target: # 중간점 값 > 찾는값
            end = mid - 1 #end 수정

        else:# 중간점 값 < 찾는값
            start = mid + 1 #start 수정
    return None

#----------------------------------------------------------------------------------
# n(원소의 개수) target(찾는 값) 입력
n, target = list(map(int, input().split()))

# 전체 원소
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
