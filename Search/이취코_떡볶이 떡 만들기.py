n,m=map(int, input().split())
array=list(map(int, input().split()))
array.sort()

start=0
end= max(array)
result=0

while start <= end:
    total=0
    mid = (start + end) // 2 #중간점

    for x in array: # 잘린 떡 길이
        if x > mid:
            total += x-mid

    if total < m: #잘린 양이 부족할 경우: 절단기 높이 감소
        end=mid-1

    else: # 잘린 양이 많을 경우 : 절단기 높이 높임
        result=mid
        start = mid + 1

print(result)
